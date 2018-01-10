from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import csv

usernameStr = 'c0000004812'
passwordStr = 'abcd'
eanText = []
ivatoText = []
descText = []
product_class = []
# list1 = ["%.2d" % i for i in range(2,48)]
# list1 = ["%.2d" % i for i in range(2,5)]
# list1 = ["%.2d" % i for i in range(5,20)]
# list1 = ["%.2d" % i for i in range(20,39)]
list1 = ["%.2d" % i for i in range(39,48)]

list2 = []
page_org = 'http://www.kinghome.it/theme1/?home&flCode='
for i in list1:
    list2.append(page_org+i)

def getProducts():
    pageSource = browser.page_source
    # print(pageSource)
    bsObj = BeautifulSoup(pageSource, "lxml")
    # print(bsObj)
    descriptions = bsObj.findAll('div', {'class': 'property name'})
    prices = bsObj.findAll('div', {'class': 'property price'})
    barcodes = bsObj.findAll('div', {'class': 'property barcode'})
    # current_class = bsObj.findChild('div', {'class': 'sub-title selected '}).contents[0]
    # current_class = browser.find_element_by_xpath("//div[@class='sub-title selected']/a")
    # / html / body / main / aside / ul / li[3] / div / a
    # print(descriptions)
    for description in descriptions:
        # print(description.get_text())
        descText.append(description.get_text())
    for price in prices:
        price = str(price.text).strip('€')
        ivatoText.append(price)
    for barcode in barcodes:
        eanText.append(barcode.get_text())
        product_class.append(current_class.get_text())
        print(barcode.get_text())
        print(current_class.get_text())



# browser = webdriver.PhantomJS(executable_path='C:/Users/lk235/Anaconda3/phantomjs-2.1.1-windows/bin/phantomjs')
browser = webdriver.PhantomJS(executable_path='D:/ProgramData/Anaconda3/phantomjs-2.1.1-windows/bin/phantomjs')

# browser = webdriver.Chrome(executable_path='D:/ProgramData/Anaconda3/chromedriver_win32/chromedriver')
# browser = webdriver.Chrome(executable_path='C:/Users/lk235/Anaconda3/chromedriver_win32/chromedriver')
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

for page in list2:
    browser.get(page)
    time.sleep(10)
    pageSource = browser.page_source
    bsObj = BeautifulSoup(pageSource, "lxml")
    current_class = bsObj.findChild('div', {'class': 'sub-title selected '}).contents[0]
    getProducts()
    while True:
        try:
            nextPageLink = browser.find_element_by_xpath("//li[@class='item next']/a")
            nextPageLink.click()
            time.sleep(10)
            getProducts()
        except NoSuchElementException:
            break
# browser.get('http://www.kinghome.it/theme1/?home&flCode=02')



# nextPageLink = browser.find_element_by_xpath("//li[@class='item next']/a")
# print(nextPageLink)
# nextPageLink.click()
# nextPage = browser.find_element_by_link_text('下一页')


print('DONE')

# csvFile = open("C:/Users/lk235/Desktop/titago/python/test.csv",'w+',newline='',encoding='utf-8')
csvFile = open("C:/Users/Administrator/Desktop/titago/python/kinghome04.csv",'w+',newline='',encoding='utf-8')
try:
    writer = csv.writer(csvFile)
    writer.writerow(('EAN', 'DESCRIZIONE', 'IVATO','CATRGORY'))
    for i in range(0,len(eanText)):
        writer.writerow((eanText[i],descText[i],ivatoText[i],product_class[i]))

finally:
    csvFile.close()







