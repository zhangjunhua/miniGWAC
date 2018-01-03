import urllib.error
import urllib.request
from bs4 import BeautifulSoup


html = urllib.request.urlopen("http://www.baidu.com")

bsObj = BeautifulSoup(html.read(), "html.parser")


print(bsObj.title)

try:
    html = urllib.request.urlopen("https://www.google.com")
except urllib.error.HTTPError as e:
    # pass
    print(e)
except ConnectionResetError as e:
    # pass
    print(e)
except urllib.error.URLError as e:
    print(e)


else:
    print (html.read())
    if html is None:
        print("html is None")
finally:
    print("will this go on in finally?")

print("will this program go on?")

