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
with_proxy=True
if with_proxy:
    proxy=urllib.request.ProxyHandler({'http': '127.0.0.1:1080','https': '127.0.0.1:1080'})
    opener=urllib.request.build_opener(proxy)
    opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')]
    urllib.request.install_opener(opener)
content=urllib.request.urlopen(url).read().decode('utf-8')

# with open('content.pkl','wb') as f:
#     pickle.dump(content,f)

# with open('content.pkl','rb') as f:
#     content=pickle.load(f)

#load old config
with open('gui-config.json') as f:
    config = json.load(f)

oldss = config['configs']
newss=[]

bsObj = bs4.BeautifulSoup(content, "html.parser")
allssitems = bsObj.find_all(class_='hover-text')
for ssitem in allssitems:
    infos = ssitem.find_all('h4')

    ip = infos[0].find_all(id=re.compile('ip'))[0].text.strip()
    port = infos[1].find_all(id=re.compile('port'))[0].text.strip()
    pwd = infos[2].find_all(id=re.compile('pw'))[0].text.strip()
    method = infos[3].text.strip().split(':')[1]
    # print("%s %s %s %s"%(ip,port,pwd,method))
    ss={}
    ss['server']=ip
    if len(port.strip())>0:
        ss['server_port']=int(port)
    else:
        continue
    ss['password'] = pwd
    ss['method'] = method
    ss['remarks'] = ""
    ss['timeout'] = 5
    newss.append(ss)

print("%d new ss are crawled from this website."%(len(newss)))
#del duplicate server in oldss
for i in range(len(oldss)-1,-1,-1):
    for j in range(len(newss)):
        if(oldss[i]['server']==newss[j]['server']):
            del oldss[i]
            break

#add new ss to oldss
for j in range(len(newss)):
    oldss.append(newss[j])

#write to config file
with open('gui-config.json','w') as f:
    json.dump(config,f,indent=2)