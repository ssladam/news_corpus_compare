# -*- coding: utf-8 -*-
#A significant number of various "todo" for future improvement are sprinked around the code.
#   Feel free to review those items, and adjust as you see fit. #I've tried to comment
#   throughout to explain my logic. Feel free to disagree and roll your own!

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import itertools, nltk, re, os, unicodedata, importlib, yaml
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import KMeans
from sklearn.manifold import MDS
#from sklearn import metrics
from scipy.cluster.hierarchy import ward, dendrogram, cophenet, linkage
from scipy.spatial.distance import pdist
from random import randint
plt.ioff() #if you keep getting a blank pop-up figure window, run this manually in the console


#If you've never setup nltk previously, execute the following line
#nltk.download()

continue_exec = True #Do not change

#========GLOBAL VARIABLES YOU CAN CUSTOMIZE TO TWEAK BEHAVIOR============
#todo: move cluster size definitions to SOURCES (from scraper.py) so cluster sizes
#  can be customized for each source
num_term_clusters = 7 #how many clusters do you want for terms?
num_concept_clusters = 13 #how many clusters for concepts?
num_terms_in_cluster = 40 #how many of the top-terms within each cluster do you want to report?
corpus_path = "C:/Users/adams/OneDrive/Documents/Text/Scraper/" #location where corpus YAML is saved
output_path = "C:/Users/adams/OneDrive/Documents/Text/output/" #location you will output all files
script_path = "C:/Users/adams/OneDrive/Documents/Text/" #location where you have saved the collection of python files
#========GLOBAL VARIABLES YOU CAN CUSTOMIZE TO TWEAK BEHAVIOR============

#Did you forget to put the backslash at the end of your input folders?
if corpus_path[-1:] != "/": corpus_path = corpus_path + "/"
if output_path[-1:] != "/": output_path = output_path + "/"
if script_path[-1:] != "/": script_path = script_path + "/"

try:
    os.chdir(script_path)
    import phrase_dict, filter_words, ec_dict, concept_dict, weight_dict
    #Even though we just loaded the modules, if you update the dictionaries, they won't be
    #  re-imported the 2nd time you run this code, since they're already in memory.
    #  Let's force a reload, to ensure that our dictionaries are up to date!
    importlib.reload(phrase_dict)
    importlib.reload(filter_words)
    importlib.reload(ec_dict)
    importlib.reload(concept_dict)
    importlib.reload(weight_dict)
    
except:
    continue_exec=False
    print('Unable to load dictionary files. Ensure all supporting files exist.')
corpus_input = {}
try:
    with open(corpus_path+'scraped_articles.yaml') as data_file:
        corpus_input = yaml.load(data_file)
except Exception as e:
    continue_exec=False
    print(e)
    print('Unable to load previous scraped articles.')

def main():
    phrases = phrase_dict.get_phrases()
    ecs = ec_dict.get_ecs()
    filters = filter_words.get_filter()
    concepts = concept_dict.get_concepts()
    weights = weight_dict.get_weights()
    #todo: currently, weights only applies to terms. Add another weighting dict for concepts
    #todo: creation of a "colocation" dictionary, such that if a DSI contains "Sanjay Patel", we know
    #  to replace all "patel" terms with "sanjayPatel"
    if continue_exec:
        return make_magic_happen(corpus_path, output_path, phrases, ecs, filters, concepts, weights, corpus_input)
    else: print("Fault detected, halting execution")


#===========================================================
#               Helper functions
#===========================================================
def lambda_unpack(f):
    return lambda args: f(*args)

#============System to chunk individual terms into phrases ===================
def extract_candidate_chunks(text, filter_words, grammar=r'KT: {(<NN.*>+)? <NN.*>+}'):
    #strip_text = re.sub(r"[^\-\,\.\?\!\'\(\)\w\d'\s]+",'',text) #remove unicode characters
    #strip_text = re.sub(r"[^\'\!\"\#\$\&\\\'\(\)\*\+\,\-\.\/\:\;\<\=\>\?\@\[\\\\\]\^\_\`\{\|\}\~\'\w\d'\s]+",'',text) #removes unicode punctuation 
    #Note: I no longer strip all unicode characters. unicodedata helpfully does a "best near match" with ascii
    strip_text = unicodedata.normalize('NFKD', text).encode('ascii','ignore').decode('utf-8')
    #Note: now I leave all punctuation to aid with sentence tokenization
    stop_words = set(nltk.corpus.stopwords.words('english'))
    stop_words |= filter_words
    
    # tokenize, POS-tag, and chunk using regular expressions
    #todo: currently the grammar chunker noun-strings strings possessives, "trump's plan" --> "trumps plan"
    #   ideally, that should be two tokens, "trump" and "plan". Without this change you get a lot of
    #   "floater" terms unlikley to pair up. For example, if Trump was always used in a possessive, like
    #   "donald trump's trade plan", or "donald trump's rhetoric", then you'd never match with the term for just "trump".
    #   In an ideal solution, you'd keep ALL three, "donald trump" and "trade plan", and "donald trumps trade plan"
    #   in that way you'd correctly associate with "donald trump", as well as a loose association with an article on
    #   obama's "trade plan", and then a very strong link with any article also discusing "donald trumps trade plan".
    chunker = nltk.chunk.regexp.RegexpParser(grammar)
    tagged_sents = nltk.pos_tag_sents(nltk.word_tokenize(sent) for sent in nltk.sent_tokenize(strip_text))
    all_chunks = list(itertools.chain.from_iterable(nltk.chunk.tree2conlltags(chunker.parse(tagged_sent))
                                                    for tagged_sent in tagged_sents))

    candidates = [' '.join(nltk.stem.WordNetLemmatizer().lemmatize(word.lower().strip()) for word, pos, chunk in group)
        for key, group in itertools.groupby(all_chunks, lambda_unpack(lambda word, pos, chunk: chunk != 'O')) if key]
    
    #We had left standard punctuation to aid in sentence chunking. Now delete all intra-word punctuation. "f.b.i. --> "fbi"
    for idx in range(len(candidates)):
        candidates[idx] = re.sub(r"[!\"#$%&\'()*+,-./:;<=>?@\[\\\]^_`{|}~]", '', candidates[idx])
        candidates[idx] = ' '.join(candidates[idx].split())
    #Did not use string.punctuation, since we need to escape the [brackets] for re.sub
    
    #return [cand.strip() for cand in candidates if cand not in stop_words]
    #return [" ".join(cand.split()) for cand in candidates if cand not in stop_words]
    #strip again, because filtering punctuation above may re-introduce floating spaces, "% people" --> " people"
    #   now I use join/split, because we need to dig out intra-string whitespace as well
    
    return [cand for cand in candidates if cand not in stop_words]

#==========Take a single long string of text and convert it into terms / phrases========
def parse_article(dsi_text, phrase_dict, ec_dict, filter_words, grammar=r'KT: {(<NN.*>+)? <NN.*>+}'):
    dsi_sentences = nltk.sent_tokenize(dsi_text)
    ec_text = ""
    insensitive_phrase = ""
    #Before processing, let's capture combinatory-word-phrases to avoid incorrect splitting
    #   e.g., "Cash for guns" --> "cashForGuns", to prevent "cash" and "guns" indivudually
    #   Currently very wasteful iteration, done for readability. If you build a large corpus and phrase dictionaries
    #   You'd be well serviced to optimize this implementation.
    for sentence in dsi_sentences:
        for phrase, ec in phrase_dict.items():
            if phrase.lower() in sentence.lower():
                #case insenstive matching, so that "CAsh For GUNS" will equal "cash for guns"
                insensitive_phrase = re.compile(re.escape(phrase), re.IGNORECASE)
                sentence = insensitive_phrase.sub(ec, sentence)
        #Consider adding punctuation in the linkage? Will help section headers (which typically
        #   do not have punctuation) separate from the following sentence
        ec_text += ' ' + sentence
    del sentence, phrase, ec, insensitive_phrase
    #Now that EC swapping is complete, let's chunk the terms
    chunked_list = extract_candidate_chunks(ec_text, filter_words, grammar)
    #We now have a series of all terms, in lower case. Now let's swap out EC terms

    chunked_series = pd.Series(chunked_list)
    chunked_series.replace(to_replace=ec_dict, inplace=True)
    
    return pd.DataFrame(chunked_series, columns=['terms'])

#===========================================================
#               Helper function to cluster terms, concepts
#===========================================================

#=========== What is the optimal number of clusters to select?=====================
def cluster_cutoff_selection(tmatrix, title='unknown', max_cluster=20, source=''):
    Z = linkage(tmatrix, 'ward')
    #You want c to be as close to 1 as possible...
    c, coph_dists = cophenet(Z, pdist(tmatrix))
    
    #Yet another dendrogram....  commented out, since managed by magic_cluster()
    #   Feel to tinker with this one, to see which approach you prefer   
    # plt.title('Hierarchical Clustering Dendrogram')
    # plt.xlabel('sample index')
    # plt.ylabel('distance')
    # dendrogram(Z, orientation="right", labels=list(tmatrix.index))
    # plt.show()
    
    fig, ax = plt.subplots(figsize=(9, 5)) # set size
    ax.margins(0.05)
    ax.tick_params(axis= 'y', which='both', left='off', top='off', labelleft='off')
    plt.ticklabel_format(style='plain',axis='x',useOffset=False)
    for axis in [ax.xaxis, ax.yaxis]:
        axis.set_major_locator(ticker.MaxNLocator(integer=True))
    
    last = Z[(-1*max_cluster - 1):, 2]
    last_rev = last[::-1]
    idxs = np.arange(1, len(last) + 1)
    ax.plot(idxs, last_rev, label="elbow", linewidth=2)
    lgd = ax.legend(numpoints=1,  loc=0)
    acceleration = np.diff(last, 2)  # 2nd derivative of the distances
    acceleration_rev = acceleration[::-1]
    ax.plot(idxs[:-2] + 1, acceleration_rev, label="inconsistency", linewidth=2)
    ax.legend(numpoints=1,  loc=0)
    plt.title(source + ' ' + title + ' Cluster Cut-off Selection')
    #plt.show()
    plt.savefig(output_path + source + '_' + title + '_cluster_cutoff.png', bbox_extra_artists=(lgd,), bbox_inches='tight', dpi=200)
    plt.close('all') #even though we don't show the plot, you need to explicitly close to free the memory
    
#======================= Build the matrices to establish clusters=====================
def magic_cluster(input_matrix, output_path, out_name, num_clusters=5, num_terms_in_cluster=20, cluster_seed=3425, source=''):
    #todo: add logic to dynamically select optimal number of clusters
    #note: num_terms_in_cluster is only the number of terms to be REPORTED, the actual
    #   number of terms is the full collection of all terms
    
    #convert our term tf_idf into a proper matrix (get rid of extraneous columns, and transpose)    
    tfidf_matrix = input_matrix.copy()
    #were we given the terms matrix to cluster, or the concept matrix?
    if 'concept' in tfidf_matrix.columns:
        tfidf_matrix.drop(['t_count','concept','d_count','tf','idf','tf_idf','weight'], axis=1, inplace=True)
    else: tfidf_matrix.drop(['t_count','d_count','tf','idf','tf_idf','weight'], axis=1, inplace=True)
    tfidf_matrix.fillna(0, inplace=True)
    tfidf_matrix = tfidf_matrix.transpose()
    
    #Calculate cosine similarity of all terms to each other...
    dist = 1 - cosine_similarity(tfidf_matrix)
    
    #determine k-means clustering
    #km = KMeans(n_clusters=num_clusters)
    km = KMeans(n_clusters=num_clusters, init='k-means++', 
            max_iter=100, n_init=1, verbose=0, random_state=cluster_seed)
    km.fit(tfidf_matrix)
    clusters = km.labels_.tolist()
    vocab_frame = pd.DataFrame(tfidf_matrix.columns)
    
    tfidf_matrix['cluster'] = clusters
    #tfidf_matrix['cluster'].value_counts() #how many DSI belong to each cluster?
    
    #what are the top terms from each of the clusters?

    cluster_terms = {}
    cluster_names = {}
    seed_name = "B"
    if cluster_seed == 3425: seed_name = "A"
    text_file = open(output_path + source + '_' + out_name + '_clusters.' + seed_name + '.txt', "w")
    #print("Top terms per cluster:\n")
    text_file.write("Top terms per cluster:\n")
    #sort cluster centers by proximity to centroid
    order_centroids = km.cluster_centers_.argsort()[:, ::-1] 
    for i in range(num_clusters):
        terms_in_cluster = ''
        dsi_in_cluster = ''
        #print("Cluster %d words:" % i)   
        text_file.write("Cluster %d words:\n" % i)   
        for ind in order_centroids[i, :num_terms_in_cluster]:
            terms_in_cluster = terms_in_cluster + vocab_frame.iloc[ind][0] + ", "
        #print(terms_in_cluster[:-2]) #don't print the trailing ', '
        text_file.write(terms_in_cluster[:-2]) #don't print the trailing ', '
        cluster_terms[i] = terms_in_cluster[:-2]
        cluster_names[i] = cluster_terms[i].split(', ')[:4] #only use the first 4 terms to "name" the cluster
        #print()
        text_file.write('\n\n')
        for dsi in tfidf_matrix[tfidf_matrix['cluster']==i].index:
            dsi_in_cluster = dsi_in_cluster + dsi + ", "
        #print("DSI in cluster %d:" % i)
        text_file.write("DSI in cluster %d:\n" % i)
        #print(dsi_in_cluster[:-2]) #don't print the trailing ', '
        text_file.write(dsi_in_cluster[:-2]) #don't print the trailing ', '
        #print('\n\n')
        text_file.write('\n\n')
    text_file.close()
    del i, terms_in_cluster, dsi_in_cluster, ind, order_centroids, text_file
    
    
    MDS()
    # convert two components as we're plotting points in a two-dimensional plane
    #   "precomputed" because we provide a distance matrix
    #   we will also specify `random_state` so the plot is reproducible.
    mds = MDS(n_components=2, dissimilarity="precomputed", random_state=1)
    pos = mds.fit_transform(dist)  # shape (n_components, n_samples)
    xs, ys = pos[:, 0], pos[:, 1]
    
    #un-comment below to manually set up colors per clusters using a dict
    #   also, find "cluster_colors" below, and un-comment that line to enable it
    #cluster_colors = {0: '#1b9e77', 1: '#d95f02', 2: '#7570b3', 3: '#e7298a', 4: '#66a61e'}
    #un-comment the below section if you want to manually name the clusters
    #   Be certain the dictionary is the same length as your declared number of clusters
    # cluster_names = {0: 'Immigration and border control', 
    #                 1: 'American governmental policy', 
    #                 2: 'Russian interference', 
    #                 3: 'International trade', 
    #                 4: 'Tax reform'}
    
    #create data frame that has the result of the MDS plus the cluster numbers and titles
    mappedDF = pd.DataFrame(dict(x=xs, y=ys, label=clusters, title=list(tfidf_matrix.index))) 
    #group by cluster
    groups = mappedDF.groupby('label')
    # set up plot
    fig, ax = plt.subplots(figsize=(16, 12)) # set size
    ax.margins(0.05) # Optional, just adds 5% padding to the autoscaling
    #iterate through groups to layer the plot
    for name, group in groups:
        ax.plot(group.x, group.y, marker='o', linestyle='', ms=12, 
                label=cluster_names[name],
                #color=cluster_colors[name], 
                mec='none')
        ax.set_aspect('auto')
        ax.tick_params(\
            axis= 'x',          # changes apply to the x-axis
            which='both',      # both major and minor ticks are affected
            bottom='off',      # ticks along the bottom edge are off
            top='off',         # ticks along the top edge are off
            labelbottom='off')
        ax.tick_params(\
            axis= 'y',         # changes apply to the y-axis
            which='both',      # both major and minor ticks are affected
            left='off',      # ticks along the bottom edge are off
            top='off',         # ticks along the top edge are off
            labelleft='off')
    lgd = ax.legend(numpoints=1, bbox_to_anchor=(.5, -.3), loc=8, borderaxespad=0.)
    #lgd = ax.legend(numpoints=1,  loc=0)
    #add label in x,y position with the label as the DSI#
    for i in range(len(mappedDF)):
        ax.text(mappedDF.loc[i]['x'], mappedDF.loc[i]['y'], mappedDF.loc[i]['title'], size=8)  
    plt.title('DSI K-Means cluster assignment: ' + out_name)
    plt.margins(0.05, 0.1)
    #plt.show() #show the plot
    plt.savefig(output_path + source + out_name + '_kmeans.' + seed_name + '.png', bbox_extra_artists=(lgd,), bbox_inches='tight', dpi=200)
    plt.close('all') #even though we don't show the plot, you need to explicitly close to free the memory
    
    #the 2D map is done, now prepare a dendrogram to visualize how clustering splits
    linkage_matrix = ward(dist) #define the linkage_matrix using ward clustering pre-computed distances
    fig, ax = plt.subplots(figsize=(15, 30)) # set size
    ax = dendrogram(linkage_matrix, orientation="right", labels=list(tfidf_matrix.index));
    
    plt.tick_params(\
        axis= 'x',          # changes apply to the x-axis
        which='both',      # both major and minor ticks are affected
        bottom='off',      # ticks along the bottom edge are off
        top='off',         # ticks along the top edge are off
        labelbottom='off')
    plt.yticks(fontsize=14)
    plt.title('DSI Ward clustering dendrogram: ' + out_name)
    #plt.show()
    #plt.savefig(output_path + out_name + '_dendrogram' + seed_name + '.png', bbox_inches='tight', dpi=72)
    #Dendrogram is generated with ward distances on pre-computed values, it does not change based on KMeans seed
    #   Therefore, don't write out an "A", and "B" version of the dendrogram
    #   Todo: udpate dendrogram to better reflect the KMeans 2D map
    #   Recommend you start here: https://joernhees.de/blog/2015/08/26/scipy-hierarchical-clustering-and-dendrogram-tutorial/
    plt.savefig(output_path + source + '_' + out_name + '_dendrogram.png', bbox_inches='tight', dpi=200)
    plt.close('all') #clear plot from memory
    
    return tfidf_matrix

#===========================================================
#               True main program
#===========================================================

def make_magic_happen(corpus_path, output_path, phrase_dict, ec_dict, filter_words, concept_dict, weight_dict, corpus_input):
    for source in corpus_input:
        #file_list = [f for f in os.listdir(corpus_path) if os.path.isfile(os.path.join(corpus_path, f))]
        file_list = []
        for i in range(0, len(corpus_input[source]['articles'])): file_list.append('DSI-' + str(i))
    
        #   Next, let's parse each article into grammar chunks, phrases, and terms
        
        #Use the following to include adjectives and preposition / conjunction chunks
        #    e.g., automatically retain "cash for guns" rather than split, "cash", "guns"
        #    e.g., "dire days on Wall Street", rather than "dire days", "Wall Street"
        grammar_conjunctions = r'KT: {(<JJ>* <NN.*>+ <IN>)? <JJ>* <NN.*>+}'
        #Use the following to include adjective modifiers
        #    e.g., "blue car" rather than just "car"
        grammar_adjectives = r'KT: {(<JJ>* <NN.*> <NN.*>+)? <JJ>* <NN.*>+}'
        #Only chunk noun-linked sections, this is the default option if you don't specify
        #    e.g., "bird house", or "emergency road flare"
        grammar_nouns = r'KT: {(<NN.*>+)? <NN.*>+}'
        
        #convert each string-of-text into a list comprised of DataFrame-of-terms
        corpus_phrases = []
        for dsi in corpus_input[source]['articles']:
            corpus_phrases.append(parse_article(dsi['text'], phrase_dict, ec_dict, filter_words, grammar_nouns))
            #replace above 'grammar_nouns' with your preferred chunker
        del dsi
        
        #gather all terms to build our "master" list of terms
        #create a new list of all dsi, and pivot on terms for total counts
        master = pd.DataFrame()
        corpus_term_counts = []
        for i in range(0, len(file_list)):
            #corpus_phrases[i]['dsi'] = file_list[i][0:6]
            corpus_phrases[i]['dsi'] = file_list[i]
            master = pd.concat([master, corpus_phrases[i]])
            corpus_term_counts.append(pd.DataFrame(corpus_phrases[i].terms.value_counts()))
            corpus_term_counts[i].columns = (['t_count'])
            corpus_term_counts[i].loc[:,'tf'] = 0.0
        del i
        
        #calculate term frequency for INDIVIDUAL DSI
        for i in range(0, len(corpus_term_counts)):
            dsi_num_terms = corpus_term_counts[i].t_count.sum()
            for term in corpus_term_counts[i].index:
                term_count = corpus_term_counts[i].loc[term].t_count
                corpus_term_counts[i].set_value(term,'tf',float(term_count) / dsi_num_terms)
        del i,term, dsi_num_terms, term_count
        
        #The index is a mish-mash of each individual DSI. Rebuild it. (Not really necessary, just being pedantic)
        master = master.reset_index(drop=True)
        
        #count number TOTAL times a term occurs in whole corpus
        master_terms = master.terms.value_counts()
        
        term_loc_series = master.groupby(['terms','dsi']).size()
        
        masterdf_terms = pd.DataFrame(master_terms)
        masterdf_terms.columns=(['t_count'])
        masterdf_terms['concept'] = 'UNKNOWN'
        masterdf_terms['d_count'] = 0
        masterdf_terms.loc[:,'tf'] = 0.0
        masterdf_terms.loc[:,'idf'] = 0.0
        masterdf_terms.loc[:,'tf_idf'] = 0.0
        masterdf_terms.loc[:,'weight'] = 1.0
        
        non_matrix_cols = ['t_count', 'concept', 'd_count', 'tf', 'idf', 'tf_idf', 'weight']
        concept_non_matrix_cols = ['t_count', 'd_count', 'tf', 'idf', 'tf_idf', 'weight']
        
        terms_in_corpus = sum(masterdf_terms['t_count'])
        
        
        #assign each term to its concept class, if known
        indexSr = pd.Series(masterdf_terms.index).str.lower()
        for key, value in concept_dict.items():
            #must confirm the key actually exists as a term, or else it'd be shoe-horned in with blank row values
            
            #todo: major bug! "match" will return true if the BEGINNING matches, such that a search to
            #  match "hillary" will return TRUE if the set contains "hillaryClinton". Need to find way
            #  to match EXACT string, since above would kick an exception to write "hillary" if that
            #  exact key does not exist, even though "hillaryClinton" returned TRUE
            #  I want to avoid doing it with another 'for' loop, which would be an easy fix
            if(indexSr.str.match(key,case=False).any()):
                try: masterdf_terms.at[masterdf_terms.index[indexSr[indexSr==key].index[0]], 'concept'] = value
                #except: print("Key matched in " + source+ " concept search, but does not exist in term index: \""+key+"\"")
                except: continue
        del indexSr
        
        #masterdf_terms['concept'] = np.where(masterdf_terms.index.str.lower().apply(lambda x: any(x.endswith(i) for i in indexSr)), concept_dict[x],'UNKNOWN')
        
        #calcualte tf_idf statistics on the FULL SET
        for term in masterdf_terms.index:
            #count the number times term occurs in a DSI
            masterdf_terms.set_value(term,'d_count',len(term_loc_series[term]))
            #calculate tf = Term_Feq_Count / Total_Terms_In_Cohort
            term_count = masterdf_terms.loc[term]['t_count']
            masterdf_terms.set_value(term,'tf',float(term_count) / terms_in_corpus)
            #calculate idf = LOG10(#DSI / d_count)
            num_dsi = len(corpus_phrases)
            masterdf_terms.set_value(term,'idf',np.log10(float(num_dsi) / masterdf_terms.loc[term]['d_count'] ))
            #calculate tf*idf
            masterdf_terms.set_value(term,'tf_idf', masterdf_terms.loc[term]['tf'] * masterdf_terms.loc[term]['idf'] )
        del term, term_count, num_dsi
        
        #create the matrix of terms across each DSI
        for i in range(0, len(corpus_term_counts)):
            for term in corpus_term_counts[i].index:
                #masterdf_terms.set_value(term,file_list[i][0:6],corpus_term_counts[i]['tf'][term])
                masterdf_terms.set_value(term,file_list[i],corpus_term_counts[i]['tf'][term])
        del i,term
        
        #Any custom weighting to be applied?
        #   COMMENT: this is for terms. I've since moved weighting to concepts. However, no reason it can't be both.
        #   If you open this up, ensure that all terms / concepts have different names, or create another dict just for term weights
        # matrix_cols = list(set(masterdf_terms.columns) - set(non_matrix_cols))
        # for term, val in weight_dict.items():
        #     try:
        #         #todo: Fails case-sensitive matching. Fix this.
        #         if term in masterdf_terms.index:
        #             masterdf_terms.loc[term,'weight'] = val
        #             for col in matrix_cols:
        #                 masterdf_terms.loc[term,col] = masterdf_terms.loc[term,col] * val
        #         else: print('failed to assign weighting, key not found in '+source+' index:\"'+term+'\"')
        #     except: print('failed to assign weighting:\"'+term+'\"')
        # del term, val, col

        #Bit of clean-up. Delete all terms that only have a single occurance
        #IMPORTANT: you may want to comment this out to see if you're eliminating important terms
        #   I axe them for simplicty. It prevents all single terms form glomming into an "UNKNOWN" category, throwing off clustering
        #   Also saved me a TON of time from having to map the individual terms into ECs & clusters. I admit that creates some knowledge loss
        masterdf_terms.drop(masterdf_terms[masterdf_terms.t_count < 2].index, inplace=True)


        #Now build concept matrix. First we pivot by concept, and sum all columns
        masterdf_concepts = masterdf_terms.groupby(['concept']).sum()
        #weighting was for terms... it's automatically rolled into component concepts
        #  Let's delete the column, since "sum of weightings" doesn't have useful meaning.
        #masterdf_concepts.drop('weight', axis=1, inplace=True)
        #Update: now I do perform weighting on concepts. But we need to reset all values to 1
        masterdf_concepts.loc[:,'weight'] = 1.0
        
        #document count shouldn't be sum'd, we should max to find real doc count, fix those values.
        #   Note: should replace this section with more pythonic code
        for concept in masterdf_concepts.index:
            #Ignore first 7 columns to only count # of items in the DSI's
            masterdf_concepts.set_value(concept, 'd_count', masterdf_concepts.loc[concept][6:].count())
        del concept
        
        #Apply weighting to concepts
        matrix_cols = list(set(masterdf_concepts.columns) - set(concept_non_matrix_cols))
        for term, val in weight_dict.items():
            try:
                #todo: Fails case-sensitive matching. Fix this.
                if term in masterdf_concepts.index:
                    masterdf_concepts.loc[term,'weight'] = val
                    for col in matrix_cols:
                        masterdf_concepts.loc[term,col] = masterdf_concepts.loc[term,col] * val
                else: print('failed to assign weighting, key not found in '+source+' index:\"'+term+'\"')
            except: print('failed to assign weighting:\"'+term+'\"')
        del term, val, col
        
        #write the master matrix out to a CSV file
        masterdf_terms.to_csv(output_path+source+ '_' + 'master.csv')
        masterdf_concepts.to_csv(output_path+source+'_'+'master_concepts.csv')
        
        #write out all of the individual DSI to their own CSV
        # for i in range(0, len(corpus_term_counts)):
        #     #corpus_term_counts[i].to_csv(output_path + file_list[i][0:6] + '.csv')
        #     corpus_term_counts[i].to_csv(output_path + source + '_' + file_list[i] + '.csv')
        # del i
        
        #write out article summary for DSI members...
        summary_df = pd.DataFrame({'DSI': range(0, len(corpus_input[source]['articles']))})
        summary_df['DSI'] = 'DSI-' + summary_df['DSI'].astype(str)
        summary_df = summary_df.assign(link = corpus_input[source]['link_set'])
        title_list = []
        link_list = []
        for article in corpus_input[source]['articles']:
            title_list.append(article['title'])
            link_list.append(article['link'])
        summary_df = summary_df.assign(link = link_list)
        summary_df = summary_df.assign(title = title_list)
        summary_df.to_csv(output_path + source + '_summary.csv')
        
        
        #perform clustering....
        term_tfmatrix = pd.DataFrame()
        #term_tfmatrix = magic_cluster(masterdf_terms, output_path, 'terms', num_term_clusters, num_terms_in_cluster, 3425, source)
        #magic_cluster(masterdf_terms, output_path, 'terms', num_term_clusters, num_terms_in_cluster, randint(3426,100000), source)
        #cluster_cutoff_selection(term_tfmatrix, 'Terms', 20, source)
        #now cluster on concepts, instead of ECs
        concept_tfmatrix = magic_cluster(masterdf_concepts, output_path, 'concepts', num_concept_clusters, num_terms_in_cluster, 3425, source)
        magic_cluster(masterdf_concepts, output_path, 'concepts', num_concept_clusters, num_terms_in_cluster, randint(3426,100000), source)
        cluster_cutoff_selection(concept_tfmatrix, 'Concepts', 20, source)
    
    
    #return the primary variables to allow exploration in the var browser
    return (masterdf_terms, masterdf_concepts, corpus_phrases, term_tfmatrix, concept_tfmatrix)

   

#===========================================================
#               main program to kick off execution
#===========================================================   
if __name__ == '__main__':
    try:
        #Let's return the primary variables, to allow exploration in the variable browser
        (terms_matrix, concepts_matrix, dsi_text, t_tmatrix, c_tmatrix) = main()
    except Exception as e:
        print(e)
        print('Unable to continue execution')

d = {'one' : pd.Series([1., 2., 3.], index=['a', 'b', 'c']), 'two' : pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d)


def pinpointconcept(df, c_name):
    to_return = pd.DataFrame(df)
    to_return[c_name] = 0.0
    to_return[c_name][c_name] = 1.0
    return to_return

def dolookup(num):
    pd.DataFrame([corpus_input['cnn']['articles'][num]['text']]).to_clipboard(index=False, header=False)
