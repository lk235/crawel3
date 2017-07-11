from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
import re
import datetime
try:

    html = urlopen("http://www.kinghome.it/jking/index.php#")

except HTTPError as e:
    print(e)
if html is None:
    print("URL is not found")
else:
    bsObj = BeautifulSoup(html, "html.parser")
    # nameList = bsObj.findAll("span", {"class": {"a-size-base a-color-price s-price a-text-bold","a-size-small"}})
    # for name in nameList:
    #     print(name.get_text())
    # namelist = bsObj.findAll(text="Domopak Sacchi Pattumiera Media - 15 Pezzi")
    # print(len(namelist))
    print(bsObj.prettify())