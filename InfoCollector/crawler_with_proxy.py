import urllib.request
import urllib.error
import bs4
import re
import pickle
import json
import io
import http.cookiejar
import gzip
url="https://en.ishadowx.net/"
proxy=urllib.request.ProxyHandler({'http': '127.0.0.1:1080','https': '127.0.0.1:1080'})
opener=urllib.request.build_opener(proxy)
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')]
urllib.request.install_opener(opener)
html=urllib.request.urlopen(url).read().decode('utf-8')

print(html)


