from urllib.request import urlopen
from bs4 import BeautifulSoup
import re


pages = set()


def getLinks(pageUrl):
    global pages
    html = urlopen("http://en.wikipedia.org"+pageUrl)
    bsObj = BeautifulSoup(html, features="html.parser")
    try:
        print("Hi: ", bsObj.h1.get_text())
        print("1st Paragraph:\n", bsObj.find(id = "mw-content-text").findAll("p")[0])
        print("Edit Link: ", bsObj.find(id = "ca-edit").find("span").find("a").attrs['href'])
    except AttributeError:
        print("This page is missing, but its all cool")

    for link in bsObj.findAll("a", href=re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                print('........................\n'+newPage)
                pages.add(newPage)
                getLinks(newPage)

getLinks("")