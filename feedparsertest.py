#from feedgen.feed import FeedGenerator
import feedparser,html,re,requests,hashlib,listparser
from readability import Document
from xml.etree import ElementTree
import sys

def cleantext(text): #just wanna cleanup and remove html
    clean = re.compile('<.*?>')
    return html.unescape(re.sub(clean, '', text))

def extract_article(url): #rajouter choix automatique en fonction de la taille
    response = requests.get(url)
    doc = Document(response.text)
    title=doc.title()
    article=cleantext(doc.summary())
    return([title,article])#retourne le nom de l'article puis le texte


def feed_hash_check(feed):
    #regarder dans la bdd et retourne le dernier hash
    print("s")

def feed_extractor(feed):
    compil=[]
    for x in feedparser.parse(feed)['entries']:
        compil.append(extract_article(x['link']))
    print((compil[0][0]))
    lasthash = hashlib.md5((compil[0][0]).encode('utf-8')).hexdigest()
    print(lasthash)
    return(compil)
    

""""""



feed="https://www.lemonde.fr/rss/une.xml"
feed_extractor(feed)


"""

    
"""
