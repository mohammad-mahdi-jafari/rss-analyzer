import feedparser

def parse(url):
    return feedparser.parse(url)

def get_source(parsed):
    feed = parsed['feed']
    return {
        'link': feed['link'],
        'title': feed['title'],
        'subtitle': feed['subtitle'],
    }

def get_articles(parsed):

    articles = []
    entries = parsed['entries']
    for entry in entries:
        print("*"*100)
        print(entry.keys())
        try:
            tempid = entry['id']
        except:
            tempid = int(entries.index(entry))
        try:
            tempsu = entry['summary']
        except:
            continue 
        
        articles.append({
            'id': tempid,
            'link': entry['link'],
            'title': entry['title'],
            'summary': tempsu,
            'published': entry['published_parsed'],
        })
#        except:
#            articles.append({
#                'id': int(entries.index(entry)),
#                'link': entry['link'],
#                'title': entry['title'],
#                'summary': entry['summary'],
#                'published': entry['published_parsed'],
#            })
    return articles

