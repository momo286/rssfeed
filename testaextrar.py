import html,re,requests
from newspaper import Article
from readability import Document
url='https://meduza.io/feature/2018/05/24/kak-gosudarstvo-otobralo-u-samyh-bednyh-grazhdan-severnye-nadbavki-a-potom-vernulo-a-potom-opyat-otobralo'
article = Article(url)
article.download()
article.parse()

def cleantext(text):
    clean = re.compile('<.*?>')
    return html.unescape(re.sub(clean, '', text))


response = requests.get(url)
doc = Document(response.text)

#print(cleantext(doc.summary()))
#print(article.text)
#print(remove_html_tags(html.unescape(doc.summary())))
print(len(cleantext(doc.summary())))
print(len(article.text))
print(doc.title())
