from bs4 import BeautifulSoup
from  selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv

usernameStr = 'c0000004812'
passwordStr = 'abcd'

# browser = webdriver.PhantomJS(executable_path='C:/Users/lk235/Anaconda3/phantomjs-2.1.1-windows/bin/phantomjs')
# browser = webdriver.PhantomJS(executable_path='D:/ProgramData/Anaconda3/phantomjs-2.1.1-windows/bin/phantomjs')
browser = webdriver.Chrome(executable_path='D:/ProgramData/Anaconda3/chromedriver_win32/chromedriver')
browser.get("http://www.kinghome.it")

username = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.ID, "luser"))
)
username.send_keys(usernameStr)
print("send username")
password = browser.find_element_by_id('lpass')
password.send_keys(passwordStr)
print("send pass")
log_button = browser.find_element_by_id('login')
log_button.click()
print("click")
time.sleep(10)


eanText = []
ivatoText = []
descText = []

pageSource = browser.page_source
# print(pageSource)
bsObj = BeautifulSoup(pageSource,"lxml")
# print(bsObj)
descriptions = bsObj.findAll('div', {'class': 'property name'})
prices = bsObj.findAll('div', {'class': 'property price'})
barcodes = bsObj.findAll('div', {'class': 'property barcode'})
# print(descriptions)
for description in descriptions:
    print(description.get_text())
    descText.append(description.get_text())

for price in prices:
    price = str(price.text).strip('€')
    print(price)

for barcode in barcodes:
    print(barcode.get_text())
# body > main > section > ul > li:nth-child(1) > div.info > div.property.name