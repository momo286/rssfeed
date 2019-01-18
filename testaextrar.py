import html,re,requests,zlib,pprint
#from newspaper import Article
from readability import Document
from flask import Flask



a='https://meduza.io/feature/2018/05/24/kak-gosudarstvo-otobralo-u-samyh-bednyh-grazhdan-severnye-nadbavki-a-potom-vernulo-a-potom-opyat-otobralo'
b="https://mbk-news.appspot.com/region/prazdnichnyj-musornyj-kollaps-vo-mnogix-regionax-otxody-ne-vyvozyat-s-proshlogo-goda/"
c="https://meduza.io/news/2019/01/06/ssha-zablokirovali-postavki-rossiyskih-samoletov-sukhoi-superjet-v-iran"
d="https://www.wonderzine.com/wonderzine/life/life/240093-survivalism"
e="https://meduza.io/feature/2019/01/07/amerika-dlya-rossii-eto-i-utopiya-i-antiutopiya-odnovremenno"
aa=[a,b,c,d,e]
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
    

"""
print(len(extract_article(url)[0]))
print(len(extract_article(url)[1]))


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

htmla='<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd"> <html lang="en"> <head> <meta http-equiv="content-type" content="text/html; charset=utf-8"> <title>Title Goes Here</title><style> body { background-color: #ffffff; color: #444444; font-family: "Open Sans"; font-weight: 400;}</style></head>  '



htmlb='</body> </html>'



app = Flask(__name__)

@app.route('/')
def index():
    temp=""
    for tp in aa:
        xxa=extract_article(tp)[0]
        xxb=extract_article(tp)[1]
        temp=(temp+"<h1>"+xxa+"</h1><br><br><p>"+xxb+"</p>")
    return(htmla+temp+htmlb)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

