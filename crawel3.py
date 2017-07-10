from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
import re
import datetime
try:
    # html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
    # html = urlopen("https://www.amazon.it/gp/site-directory/ref=nav_shopall_btn")
    html = urlopen("https://www.amazon.it/b/ref=s9_acss_bw_ct_GroHome_ct_6_h_w?_encoding=UTF8&ie=UTF8&node=6394759031&pf_rd_m=A11IL2PNWYJU7H&pf_rd_s=merchandised-search-4&pf_rd_r=WXQTFTVQPTWB8PV63KBS&pf_rd_t=101&pf_rd_p=ddb2c7e1-8b2c-5bdb-a6b5-0f89939ab859&pf_rd_i=6198092031")
    # html = urlopen("https://s.taobao.com/list?spm=a217l.8087239.620327.1.729cb1d2la2HW0&q=%E7%94%B5%E9%A5%AD%E7%85%B2&style=grid&seller_type=taobao")
    # html = urlopen("https://www.jd.com/")
    # html = urlopen("http://www.iwencai.net/stockpick/search?typed=1&preParams=&ts=1&f=1&qs=index_rewrite&selfsectsn=&querytype=&searchfilter=&tid=stockpick&w=dde")
except HTTPError as e:
    print(e)
if html is None:
    print("URL is not found")
else:
    bsObj = BeautifulSoup(html, "html.parser")
    # nameList = bsObj.findAll("span", {"class": {"a-size-base a-color-price s-price a-text-bold","a-size-small"}})
    # for name in nameList:
    #     print(name.get_text())
    namelist = bsObj.findAll(text="Domopak Sacchi Pattumiera Media - 15 Pezzi")
    print(len(namelist))


    # for child in bsObj.find("table",{"id":""}).children:
    #     print(child)

    # for child in bsObj.find("table",{"id":""}).descendants():
    #     print(child)

    # for sibling in bsObj.find("table",{"id":""}).tr.next_siblings:
    #     print(sibling)

    # images = bsObj.findAll("img",{"src":"misc.360buyimg.com/mtd/pc/common/img/blank.png"})
    # for image in images:
    #     print(image)

    # for link in bsObj.find("div",{"id":"bodyContent"}).findAll("a",href = re.compile("^(/wiki)((?!:).)*$")):
    #     if 'href' in link.attrs:
    #         print(link.attrs['href'])

    #
    # for link in bsObj.findAll("a",{"class":"nav_a"}):
    #     if 'href' in link.attrs:
    #         print("https://www.amazon.it" + link.attrs['href'])
    #
    # for link in bsObj.find_all('a'):
    #     if str(link.get('href')).find('http') == -1 :
    #         print("https://www.amazon.it" + str(link.get('href')))
    #
    #     else:
    #         print(link.get('href'))





    # for sibling in bsObj.find("table",{"class":"static_table tbody_table static_tbody_table"}).tr.next_siblings:
    #     print(sibling)
    #
    # print(bsObj.table)
    # print(bsObj.prettify())
    # print(bsObj.title.parent.name)
    # print(bsObj.title.name)
    # print(bsObj.title.string)
    # print(bsObj.title)
    # print(bsObj.p)
    # print(bsObj.p['class'])
    # print(bsObj.a)
    # print(bsObj.find_all('a'))
    # print(bsObj.find(id="nav-search"))
    # print(bsObj.get_text())
#     print(bsObj.a.attrs)
# print(bsObj.p.attrs)






# 打印图片对应商品价格
#     print(bsObj.find("img",{"src":"../img/gifts/img1.jpg"}).parnet.previous_sibling.get_text())


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

