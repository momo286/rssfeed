import feedparser
from readability import Document
import html,re,requests,zlib,pprint


def cleantext(text): #just wanna cleanup and remove html
    clean = re.compile('<.*?>')
    return html.unescape(re.sub(clean, '', text))

def extract_article(url): #rajouter choix automatique en fonction de la taille
    """
    article = Article(url)
    article.download()
    article.parse()
    t1=article.title
    a1=article.text
    """
    response = requests.get(url)
    doc = Document(response.text)
    t2=doc.title()
    a2=cleantext(doc.summary())
    return([t2,a2])
    

"""https://batenka.ru/rss_zen/"""

"""https://habr.com/ru/rss/best/daily/?fl=ru"""
d = feedparser.parse("https://habr.com/ru/rss/best/daily/?fl=ru")
for x in d:
    print(x)
print

"""
for x in d['entries']:
    tmp=extract_article(x['link'])
    print(tmp[0])
    print(len(tmp[1]))
    
"""
