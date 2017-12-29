
import urllib.request
from bs4 import BeautifulSoup


html = urllib.request.urlopen("http://www.baidu.com")

bsObj = BeautifulSoup(html.read(), "html.parser")

print(bsObj.html)


