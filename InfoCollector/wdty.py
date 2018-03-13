import urllib.request
import urllib.error
import bs4
import re
import json
import io
import http.cookiejar
import gzip
# import xlwt

'''
(id,2368)
(plat_name,宜人贷)
(plat_id,5)
(create_time,1513750213)
(update_time,1513825742)
(rate,11.67)
(level,A+)
(score,95.68)
(claims,45.64)
(standard,875.37)
(limit,3.18)
(operation,44.07)
(regional,24.38)
(investment,2.09)
(borrowing,2.42)
(liquidity,160.18)
(year,2017)
(month,12)
(change,0)
(xscore,70.00)
(hscore,83.00)
(city,北京)
(shangxian_time,2012-07)
(domain_body,yirendai)
(interest_rate,5%~9.6%)
(is_fl,1)
(flurl,http://www.p2peye.com/rebate/5-1-2.html)
(level_number,1)
(is_loans,)
(loanlink,http://licai.p2peye.com/loans/newuser/b0r0t0l5d0p1.html)	
'''
att2col={'id':'平台id','plat_name':'平台名称','rate':'利率','level':'等级','score':'数据评分','claims':'偿兑性',
         'standard':'资金流入率','limit':'期限','operation':'运营','regional':'地域性','borrowing':'','':'','':'','':'','':'','':'','':''}
# cookiestr='__jsluid=8590ba3bf2bd187ff73a070e24ce2ba8; A4gK_987c_saltkey=jEe36X88; A4gK_987c_lastvisit=1514903545; TYID=enANiFpLpgkKvA8LDbs1Ag==; __firstReferrerKey__=%7B%22%24first_referrer%22%3A%22http%3A%2F%2Fwww.p2peye.com%2Frating%22%2C%22%24first_referrer_host%22%3A%22www.p2peye.com%22%7D; Hm_lvt_556481319fcc744485a7d4122cb86ca7=1514907149; __jsl_clearance=1514944731.82|0|wmfmUKvZeRrZ%2BFhdrI6R%2B3HHkW8%3D; bdp_data2017jssdkcross=%7B%22distinct_id%22%3A%22160b780a376269-09669f08088105-5a442916-1327104-160b780a37746%22%2C%22props%22%3A%7B%22user_id%22%3A0%2C%22%24is_first_session%22%3A0%7D%7D; A4gK_987c_lastact=1514945196%09ajax.php%09portallist; Hm_lpvt_556481319fcc744485a7d4122cb86ca7=1514945199; __bdpa_session_key__2017__=%7B%22session_time%22%3A1514945201465%2C%22session_id%22%3A%22160b9be485446-00bf5760852faf-5a442916-1327104-160b9be48554b2%22%2C%22session_hasBeenExpired%22%3A0%2C%22lastSend_sessonId%22%3A%22160b9be485446-00bf5760852faf-5a442916-1327104-160b9be48554b2%22%7D'
cookiestr="__jsluid=310c6dbb59b1980b1ebfa4b1848c3c1b;"
def processJson(str):
    doc = json.loads(str)
    for dict in doc:
        print(len(dict))
        for k, v in dict.items():
            print("(%s,%s)"%(k,v),end='\t')
        print()

def getInfo():
    try:


        # headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.2) Gecko/20100103 Firefox/23.0',
        #            'Cookie':'__jsluid=9ff36f84fd8fa9a67e87ef9201ff8797; A4gK_987c_saltkey=XB8WBzOi; A4gK_987c_lastvisit=1514902129; TYID=enANiFpLoIGiIQ8PFNRjAg==; bdp_data_is_new_user=true; __firstReferrerKey__=%7B%22%24first_referrer%22%3A%22http%3A%2F%2Fwww.p2peye.com%2Frating%22%2C%22%24first_referrer_host%22%3A%22www.p2peye.com%22%7D; Hm_lvt_556481319fcc744485a7d4122cb86ca7=1514905734; __jsl_clearance=1514906351.329|0|Eb%2FxB%2BaRieQBgj4v5FBIL4xsqaI%3D; A4gK_987c_sendmail=1; bdp_data2017jssdkcross=%7B%22distinct_id%22%3A%22160b76b068440b-01a2d4caaa193a-5a442916-1327104-160b76b068529e%22%2C%22props%22%3A%7B%22user_id%22%3A0%2C%22%24is_first_session%22%3A0%7D%7D; A4gK_987c_lastact=1514906360%09ajax.php%09ad; __bdpa_session_key__2017__=%7B%22session_time%22%3A1514906361045%2C%22session_id%22%3A%22160b76b069cb6-0b48dc993e9738-5a442916-1327104-160b76b06a11c1%22%2C%22session_hasBeenExpired%22%3A0%2C%22lastSend_sessonId%22%3A%22160b76b069cb6-0b48dc993e9738-5a442916-1327104-160b76b06a11c1%22%7D; Hm_lpvt_556481319fcc744485a7d4122cb86ca7=1514906362'
        #            }
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding':'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection':'keep-alive',
            # 'Cookie': cookiestr,
            'Host':'www.p2peye.com',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
        }
        # headers = {
        #     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        #     'Accept-Encoding':'gzip, deflate',
        #     'Cookie': 'TYID=enANiFnLKkd61S4xH1W0Ag==; __jsluid=649aa12fbaf2e39058f8f4bb33770bf8; A4gK_987c_nofavfid=1; A4gK_987c_ulastactivity=1507204828%7C0; A4gK_987c_connect_is_bind=0; __firstReferrerKey__=%7B%22%24first_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3D8Iy5HsusuYTHyi6c6y7AVq69sFcYoCbF_XvmtlXW0Ae%26wd%3D%26eqid%3Df21f492e0002a0d6000000035a0b187a%22%2C%22%24first_referrer_host%22%3A%22www.baidu.com%22%7D; A4gK_987c_saltkey=Y8Zw2H2z; A4gK_987c_lastvisit=1512487893; TY_SESOURCE=se_baidu; A4gK_987c_visitedfid=60D81D65; Hm_lvt_556481319fcc744485a7d4122cb86ca7=1512491496,1514617662,1514715056,1514883976; __jsl_clearance=1514903201.556|0|0lKJ9pFseax4n6IZf2g%2BPlxb9ic%3D; A4gK_987c_sendmail=1; bdp_data2017jssdkcross=%7B%22distinct_id%22%3A%2215fbb58484ee1-0b9b0a6c2586f1-5b44271d-1327104-15fbb584856d3%22%2C%22props%22%3A%7B%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DOqHm6StCOi6vdb31eJcLSs6P9cFZJiS4eDIWjIea6di%26wd%3D%26eqid%3D97848c590002b1e7000000045a48b7a5%22%2C%22%24latest_referrer_host%22%3A%22www.baidu.com%22%2C%22user_id%22%3A0%2C%22check_params%22%3A%22isExpired%3Dfalse%26lastSessionTime%3D1510676941329%26bdpa_session_isExpired%3Dfalse%26sessionStore%3D%7B%5C%22session_time%5C%22%3A1510676941329%2C%5C%22session_id%5C%22%3A%5C%2215fbb58487e5c-05397f4d9a6521-5b44271d-1327104-15fbb584882fa%5C%22%2C%5C%22session_hasBeenExpired%5C%22%3A0%2C%5C%22lastSend_sessonId%5C%22%3A%5C%2215fbb58487e5c-05397f4d9a6521-5b44271d-1327104-15fbb584882fa%5C%22%7D%22%2C%22%24is_first_session%22%3A0%7D%7D; A4gK_987c_lastact=1514903212%09ajax.php%09ad; __bdpa_session_key__2017__=%7B%22session_time%22%3A1514903215654%2C%22session_id%22%3A%22160b7448f983c3-098f8aca7ebc34-5a442916-1327104-160b7448f99450%22%2C%22session_hasBeenExpired%22%3A0%2C%22lastSend_sessonId%22%3A%22160b7448f983c3-098f8aca7ebc34-5a442916-1327104-160b7448f99450%22%7D; Hm_lpvt_556481319fcc744485a7d4122cb86ca7=1514903216',
        #     'Host':'www.p2peye.com',
        #     'Upgrade-Insecure-Requests': '1',
        #     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
        # }
        cookie=http.cookiejar.CookieJar()
        handler=urllib.request.HTTPCookieProcessor(cookie)
        opener=urllib.request.build_opener(handler)

        req=urllib.request.Request(url="http://www.p2peye.com/rating", headers=headers)
        # html = urllib.request.urlopen(req)
        html = opener.open(req)
        content=html.read()
        buf = io.BytesIO(content)
        gf = gzip.GzipFile(fileobj=buf)
        content2 = gf.read()
        print(content2)
        print(content2.decode('gbk'))
        print(type)
        bsObj = bs4.BeautifulSoup(content2.decode('gbk'))
        scriptlist = bsObj.find_all("script")
        for script in scriptlist:
            if "var PLATDATAJSON" in script.get_text():
                pattern = re.compile(r'\[.*\]')
                match = pattern.search(script.get_text())
                # match = pattern.search(r"ON = [abd]kldj")
                if match:
                    rslt=match.group()
                    rslt=rslt.replace("'",'"')
                    processJson(rslt)
                else:
                    print("no match found!")
    except urllib.error.HTTPError as e:
        print(e)
    for item in cookie:
        print('Name = ' + item.name)
        print('Value = ' + item.value)

if __name__ == '__main__':
    getInfo()
    # accessExcel()

