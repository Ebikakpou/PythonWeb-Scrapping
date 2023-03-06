from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://pythonscraping.com/pages/page1.html")
bsObj = BeautifulSoup(html.read(), features="html.parser")
#bsObj = BeautifulSoup(html.read(), 'lxml')
print(bsObj.prettify)
