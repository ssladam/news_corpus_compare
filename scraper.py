import yaml, bs4
import feedparser as fp
import newspaper #https://github.com/codelucas/newspaper
from time import mktime
from datetime import datetime

# Set the limit for number of articles to download
LIMIT = 100 #upper limit for max # articles to read it at any one time
MIN_TEXT = 550 #minimum number of valid characters to be considered for inclusion

data = {}
script_path = "C:/Users/adams/OneDrive/Documents/Text/Scraper/" #location where corpus YAML is saved
if script_path[-1:] != "/": script_path = script_path + "/"

sources = {
            "cnn": {
                "rss": "http://rss.cnn.com/rss/cnn_allpolitics.rss",
           	    "link": "http://edition.cnn.com/"
            },
            "wapo": {
                "rss": "http://feeds.washingtonpost.com/rss/rss_election-2012",
                "link": "https://www.washingtonpost.com/"
            },
            "reddit": {
                "rss": "http://www.reddit.com/r/politics.rss",
           	    "link": "http://www.reddit.com/r/politics/"
            },
            "foxnews": {
                "rss": "http://feeds.foxnews.com/foxnews/politics",
           	    "link": "http://www.foxnews.com/"
            },
            "nbcnews": {
                "rss": "http://feeds.nbcnews.com/feeds/nbcpolitics",
           	    "link": "http://www.nbcnews.com/"
            },
            "buzzfeed": {
                "rss": "http://www.buzzfeed.com/politics.xml",
           	    "link": "http://www.buzzfeed.com/"
            }
        }

try:
    with open(script_path+'scraped_articles.yaml') as data_file:
        data = yaml.load(data_file)
except Exception as e:
    print(e)
    print('Unable to load previous scraped articles.')


config = newspaper.Config()
config.fetch_images = False
config.memoize_articles=False

#iterate through all sources. Stop after RSS feed exhausted, or LIMIT reached
for source, value in sources.items():
    site = {
        "rss": value['rss'],
        "link": value['link'],
        "articles": [],
        "link_set": set()
    }
    count = 1
    print("Capturing articles from", source)
    d = fp.parse(value['rss'])
    if source not in data:
        #data[source] = site #first run? add blank site to master list
        data[source] = {"rss": value['rss'],"link": value['link'],"articles": [],"link_set": set()}
    for entry in d.entries:
        article = {}
        if source in 'reddit':
            soup = bs4.BeautifulSoup(entry['summary'],'html.parser')
            entry.link = soup.find_all('a')[2].get('href')
        if entry.link not in data[source]['link_set']:
            #print('new article!')
            article['link'] = entry.link
            article['scanned'] = datetime.now().isoformat()
            try:
                date = entry.published_parsed
                article['published'] = datetime.fromtimestamp(mktime(date)).isoformat()
            except:
                #try/except since some dates are improper format, and throw an error
                print('no valid published date')
            try:
                content = newspaper.Article(entry.link, config)
                content.download()
                content.parse()
            except Exception as e:
                print(e)
                continue #unable to download / parse article, break out of this iteration
            article['title'] = content.title
            article['text'] = content.text
            site['articles'].append(article)
            site['link_set'].add(entry.link)
            print(count, "articles downloaded from", source, ", url: ", entry.link)
            count = count + 1 #used a counter, not enumerate, so only increments after valid data capture
            if count > LIMIT:
                print('limit reached!')
                break
        #else: print('in set already!')
    data[source]['articles'] += site['articles']
    data[source]['link_set'] |= site['link_set']

#Some of our articles may be malformed. Let's get rid of empty articles, and/or articles that are too short
#  Note: we remove the short articles links from our previously scanned set. Maybe on re-scan a failed
#  article will be captured?
#  Side effect: junk, too short articles will be scanned every time
clean_data = {}
for source, value in data.items():
    clean_data[source] = {"rss":value['rss'], "link":value['link'],"articles":[],"link_set":set()}
    for article in data[source]['articles']:
        if(len(article['text']) > MIN_TEXT):
            #print(len(article['text']))
            #print(article['link'])
            clean_data[source]['articles'].append(article)
            clean_data[source]['link_set'].add(article['link'])
            


try:
    with open(script_path+'scraped_articles.yaml', 'w') as outfile:
        yaml.dump(clean_data, outfile, default_flow_style=False)
except Exception as e: print(e)


