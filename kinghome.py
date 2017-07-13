from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
import re
import datetime
import requests
from requests.auth import AuthBase
from requests.auth import HTTPBasicAuth
from selenium import webdriver
import time

username="c0000004812"
passwd="abcd"
browser = webdriver.Chrome("D:\ProgramData\Anaconda3\chromedriver_win32\chromedriver")
browser.get('http://www.kinghome.it/jking/index.php#log')
browser.implicitly_wait(10)
elem=browser.find_element_by_id("user")
elem.send_keys(username)
elem=browser.find_element_by_id("pass")
elem.send_keys(passwd)
elem=browser.find_element_by_id("dolog")
elem.click()
browser.implicitly_wait(10)
print()

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

