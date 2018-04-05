# news_corpus_compare
Scrape various news feeds to build and compare contents

You can consider "scraper.py" to be the first bit of code you need to execute. In that file you have the option to define all sources you wish to extract content, the maximum number of articles to capture in any one go, and the minimum length of an article to be considered for inclusion. The code is currently configured to ONLY extract articles from RSS feeds, and the link to the main site is simply included as a reference point. Please note that you will likely need to run the this RSS scraper once every day or so for several days, since typically RSS feeds only provide the XX most recent published articles.

Scraped articles are saved into a YAML file, which is then opened by the "work-horse" program, scrape_cluster.py. You will need to edit the paths in both scraper.py and scrape_cluster.py to folders on your local system. Also note, there is an expectation that you edit all of the supporting files to match your corups:
- filter_words: a library of terms you wish to exclude
- phrase_dict: generate a dictionary of phrases to be replaced with custom text to prevent the grammar chunker from breaking up words you want to stick together
- ec_dict: map all terms which have equivalent meaning into a single term
- concept_dict: map all EC terms into their more broad conceptual categories
- weight_dict: apply weighting to concepts to aid in clustering

I have included a "dictionary generator" excel file, which should help in the quick-and-easy creation or update of the above listed dictionaries.

In the /article_input/ folder I've included the corpus of material I used for my quick analysis.

An important note: since I want to avoid re-reading the same article many times, I will capture the RSS link and add it into a set of links already captured. In general it works, but if a source update the link to the same article (maybe they make a correction?) it will cause the same article to be captured multiple times. Currently NBC News in the sample set has several duplicates. Ideally the comparison should be updated with a "fuzzy match" logic to prevent this sort of behavior.

I have included sample output from this code in the /sample_output/ folder. A quick comment on the files:
- Each source will have a <source>_summary.csv generated to quickly report which articles were captured, and provide their link and article title
- <source>_concepts_cluster_cutoff.jpg provides a cluster-cutoff analysis chart
- <source>_concepts_cluster.X.txt provides a summary of each cluster, as well as a list of all DSI in each cluster. This is especially useful if many DSI overlap on the KMeans chart, making it hard to read the DSI number
- Each time I generate two cluster maps, one with a fixed seed in "A", and another with a random seed in "B". You can use "A" for reproduceable results on every iteration, and then you can use "B" to validate the results (ideally, very few DSI will hop between different clusters, and the terms will stay generally the same)
- <source>_master.csv is the "master" summary of all terms, including their mapped concept assignment. This is the primary file you should be using to capture which terms you want to filter, which still need to be mapped to an EC, and which ones still need a concept assignment. Other than serving as a working document, you won't need it in the end. This file is essentially the TF_IDF matrix with a few extra columns. Once you've finished capturing terms you're likely to spend most of your time reviewing the cluster maps.
- <source>_master_concepts.csv you likely will never need, but it is the core of what is used to generate the concept cluster map

Note: the code includes the ability to generate term-cluster maps in addition to the current concept-map. However, for that to have any real meaning you'd like want to perform LDA mapping, otherwise the term-clusters will look like noise in a KMeans map.
