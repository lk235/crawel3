from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
import re
import datetime
import requests
from requests.auth import AuthBase
from requests.auth import HTTPBasicAuth
from  selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import csv
import pymysql

usernameStr = 'c0000004812'
passwordStr = 'abcd'
# conn = pymysql.connect(host='127.0.0.1', user='lk235',passWd='None',db='python')
# cur = conn.cursor()
# cur.execute('select * from kinghome')
# print(cur.fetchone())
# cur.close()
# conn.close()
# csvFile = open("C:/Users/Administrator/Desktop/titago/python/test.csv",'w+')

# browser = webdriver.PhantomJS(executable_path='D:/ProgramData/Anaconda3/phantomjs-2.1.1-windows/bin/phantomjs')
# browser = webdriver.Chrome(executable_path='D:/ProgramData/Anaconda3/chromedriver_win32/chromedriver')
# browser = webdriver.Chrome(executable_path='C:/Users/lk235/Anaconda3/chromedriver_win32/chromedriver')
browser = webdriver.PhantomJS(executable_path='C:/Users/lk235/Anaconda3/phantomjs-2.1.1-windows/bin/phantomjs')
browser.get("http://www.kinghome.it/jking/index.php#log")

username = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.ID, "user"))
)

# username = browser.find_element_by_id('user')
username.send_keys(usernameStr)
print("send username")
password = browser.find_element_by_id('pass')
password.send_keys(passwordStr)
print("send pass")
log_button = browser.find_element_by_id('dolog')
log_button.click()
print("click")
time.sleep(10)

# eans = browser.find_elements_by_xpath("//div/table/tbody/tr[1]/td[2]")
# for ean in eans:
#     print(ean.text)

# print(browser.find_element_by_class_name('description').)
# print(browser.find_element_by_xpath('//div[@class="hideblock"]/table/tbody/tr[2]/td').text )
eanText = []
ivatoText = []
descText = []

def getproduct():

    prices = browser.find_elements_by_class_name('final-price')
    for price in prices:
        price = str(price.text).strip('€')
        print(price)
        ivatoText.append(price)



    pageSource = browser.page_source
    bsObj = BeautifulSoup(pageSource)
    descriptions = bsObj.findAll('div', {'class': 'description'})
    for description in descriptions:
        print(description.get_text())
        descText.append(description.get_text())


    eans = browser.find_elements_by_xpath("//li/table/tbody/tr[1]/td[2]")
    for ean in eans:
        print(ean.text)
        eanText.append(ean.text)

nextPage = browser.get('http://www.kinghome.it/jking/product/?fl=&lang=zh-cn')
time.sleep(5)
getproduct()
count = 1
page = 1

while count < 393:
    nextPageLink = browser.find_element_by_id('next')

    # try:
    #     nextPageLink = browser.find_element_by_id('next')
    # except NoSuchElementException:
    #     print('break')
    #     break

    # try:
    #     nextPageLink = WebDriverWait(browser, 10).until(
    #         EC.presence_of_element_located((By.ID, "next"))
    #     )
    # except :
    #     break


    nextPageLink.click()
    time.sleep(5)
    getproduct()
    count = count + 1
    print('page'+ str(count))


csvFile = open("C:/Users/lk235/Desktop/titago/python/test.csv",'w+',newline='',encoding='utf-8')
# csvFile = open("C:/Users/Administrator/Desktop/titago/python/test.csv",'w+',newline='',encoding='utf-8')
try:
    writer = csv.writer(csvFile)
    writer.writerow(('EAN', 'DESCRIZIONE', 'IVATO','COMPANY'))
    for i in range(0,len(eanText)):
        writer.writerow((eanText[i],descText[i],ivatoText[i],'kinghome'))

finally:
    csvFile.close()













# for link in bsObj.findAll('a'):
#     if 'href'in link.attrs:
#         print(link.attrs['href'])
# print(bsObj)

# print(browser.get_cookies())
# print(browser.find_element_by_id('').text)









# try:
    # username = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.ID, "user"))
    # )
    # username.send_keys("c0000004812")
    # print("username done")
    # password = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.ID, "pass"))
    # )
    # password.send_keys("abcd")
    # print("password done")

    # log_button = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.ID, "dolog"))
    # )

    # print("finally")
# username = driver.find_element_by_id("user")
# username.send_keys("c0000004812")
# password = driver.find_element_by_id("pass")
# password.send_keys("abcd")
# button = driver.find_element_by_id("dolog")
# button.click()


# finally:

# driver.close()
# time.sleep(10)
# driver.implicitly_wait(20)

# password = driver.find_element_by_name("pass")

# form = driver.find_element_by_id('login')
# form.submit()
# time.sleep(10)
# print(driver.find_element_by_id('section').text)

# username="c0000004812"
# passwd="abcd"
# browser = webdriver.Chrome("C:\Users\lk235\Anaconda3\chromedriver_win32\chromedriver")
# browser.get('http://www.kinghome.it/jking/index.php#log')
# browser.implicitly_wait(10)
# elem=browser.find_element_by_id("user")
# elem.send_keys(username)
# elem=browser.find_element_by_id("pass")
# elem.send_keys(passwd)
# elem=browser.find_element_by_id("dolog")
# elem.click()
# browser.implicitly_wait(10)
# print()

# driver = webdriver.PhantomJS(executable_path='D:/ProgramData/Anaconda3/phantomjs-2.1.1-windows/bin/phantomjs')
# driver.get("http://www.kinghome.it/jking/index.php#log")
# time.sleep(3)
# print(driver.find_element_by_id('content').text)
# driver.close
#
# loginUrl = ""

# auth = HTTPBasicAuth('c0000004812','abcd')
# r = requests.post("http://www.kinghome.it/jking/index.php#log",auth=auth)
# print(r.text)

# params = {'user':'c0000004812', 'pass':'abcd'}
# r = requests.post("http://www.kinghome.it/jking/index.php#",data=params)
# html = urlopen("http://www.kinghome.it/jking/index.php#





# print(r.cookies.get_dict() )
# r = requests.get("http://www.kinghome.it/jking/index.php#", cookies=r.cookies)
# print(r.text)

