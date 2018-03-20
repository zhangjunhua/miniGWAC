from splinter.browser import Browser
from time import sleep
import traceback
import time, sys
import codecs
import argparse
import os
import time

drivername="chrome"
driverpath="C:/Users/admin/PycharmProjects/miniGWAC/resource/chromedriver.exe"
driver=Browser(driver_name=drivername,executable_path=driverpath)

driver.visit("https://mail.qq.com/cgi-bin/frame_html")

while True:
    if "loginpage" in driver.url:
        print("wait for login")
        sleep(1)
    else:
        print("login success")
        break

driver.find_by_id("frame_html_setting")[0].click()

def delete(driver):
    with driver.get_iframe("mainFrame") as iframe:
        recieveRule =iframe.find_by_text(u"收信规则")
        recieveRule[0].click()
        dellist=iframe.find_by_text(u"删除")
        if len(dellist)>0:
            dellist.first.click()
    sleep(1)
    comfirm=driver.find_by_id("QMconfirm_QMDialog_confirm")
    comfirm.click()

delete(driver)


#//https://mail.qq.com/cgi-bin/frame_html?sid=_V-NGFeAfY0ihAtR&r=da23c49fbc52c237ffb741646bd8b330