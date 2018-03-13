import urllib.request
import urllib.error
import bs4
import re
import pickle
import json
import io
import http.cookiejar
import gzip

html = urllib.request.urlopen("https://global.ishadowx.net")
content = html.read().decode('utf-8')

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
    ss['server_port']=int(port)
    ss['password'] = pwd
    ss['method'] = method
    ss['remarks'] = ""
    ss['timeout'] = 5
    newss.append(ss)


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