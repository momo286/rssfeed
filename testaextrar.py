import html,re,requests,zlib
from newspaper import Article
from readability import Document

url='https://meduza.io/feature/2018/05/24/kak-gosudarstvo-otobralo-u-samyh-bednyh-grazhdan-severnye-nadbavki-a-potom-vernulo-a-potom-opyat-otobralo'

def cleantext(text): #just wanna cleanup and remove html
    clean = re.compile('<.*?>')
    return html.unescape(re.sub(clean, '', text))

def extract_article(url):
    print("e")
    article = Article(url)
    article.download()
    article.parse()
    
    response = requests.get(url)
    doc = Document(response.text)
    
    return([article.text,cleantext(doc.summary())])
    

print(len(extract_article(url)[1]))

"""
article = Article(url)
article.download()
article.parse()


response = requests.get(url)
doc = Document(response.text)

aa=cleantext(doc.summary())

bb=article.text

#print(cleantext(doc.summary()))
#print(article.text)
#print(remove_html_tags(html.unescape(doc.summary())))
print(len(cleantext(doc.summary())))
print(len(article.text))
print(doc.title())

b=aa.encode()
c = zlib.compress(b, 9)
print(len(b))
print(len(c))



import zlib

a="Depuis deux mois, des centaines de migrants, majoritairement iraniens, ont tenté de traverser la Manche sur des canots pneumatiques pour rejoindre l’Angleterre, poussant le ministre de l’intérieufghdfgldfgkd,fkg ,dfkgn, dkfngjd nfgj ndjfngjdnfgjdnfgjdfngr britannique, Sajid Javid, à déclarer un « incident majeur » et à rentrer précipitamment de ses vacances dimanche 30 décembre. Après un échange téléphonique avec son homologue français, Christophe Castener, il a annoncé un renforcement de la surveillance des plages et de la mer. Les Britanniques vont notamment financer des drones et des caméras pour surveiller la dizaine de points d’embarquement qui a été identifiée en France"

b=a.encode()
c = zlib.compress(b, 9)
print(len(b))
print(len(c))
"""
