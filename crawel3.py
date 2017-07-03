from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
try:
    html = urlopen("http://www.iwencai.com/stockpick/search?typed=1&preParams=&ts=1&f=1&qs=index_rewrite&selfsectsn=&querytype=&searchfilter=&tid=stockpick&w=dde")
except HTTPError as e:
    print(e)
if html is None:
    print("URL is not found")
else:
    bsObj = BeautifulSoup(html)
    nameList = bsObj.findAll("li", {"class":"channel_item"})
    for name in nameList:
        print (name.get_text())

# def getTitle(url):
#     try:
#         html = urlopen(url)
#     except HTTPError as e:
#         return None
#     try:
#         bsObj = BeautifulSoup(html.read())
#         title = bsObj.body.h1
#     except AttributeError as e:
#         return None
#
#     return title
#
# title = getTitle("http://www.iwencai.com/stockpick/search?typed=1&preParams=&ts=1&f=1&qs=index_rewrite&selfsectsn=&querytype=&searchfilter=&tid=stockpick&w=dde")
# if title == None:
#     print("Title could not be found")
# else:
#     print(title)

