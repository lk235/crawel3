from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
import re
import datetime
import requests

params = {'user':'c0000004812', 'pass':'abcd'}
r = requests.post("http://www.kinghome.it/jking/index.php#",data=params)
# html = urlopen("http://www.kinghome.it/jking/index.php#")


print(r.text)