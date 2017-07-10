from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
import re
import datetime

def getDDE(date):
    try:
        url = "http://www.iwencai.net/stockpick/search?typed=1&preParams=&ts=1&f=1&qs=result_rewrite&selfsectsn=&querytype=&searchfilter=&tid=stockpick&w=" + date +"%20dde&queryarea="
        html = urlopen(url)
    except HTTPError as e:
        print(e)

    if html is None:
        print("URL is not found")
    else:
        print(str(date))
        bsObj = BeautifulSoup(html, "html.parser")
        nameList = bsObj.findAll("div", {"class": "em graph alignCenter graph"})
        for name in nameList:
            print(name.get_text())

begin = datetime.date(2017,7,1)
end = datetime.date(2017,7,7)
for i in range((end-begin).days + 1):
    day = begin + datetime.timedelta(days=i)
    getDDE(str(day))
