#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 16:55:50 2018

@author: zhangsan
"""
from selenium import webdriver
import time
import pandas as pd
browser=webdriver.Chrome()
browser.get("https://twitter.com/vechainofficial")
browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
time.sleep(10)
browser.execute_script('alert("To Bottom")')
time.sleep(5)
timestamp_today=browser.find_elements_by_xpath('//span[contains(@class,"_timestamp js-short-timestamp js-relative-timestamp")]')
abstract= browser.find_elements_by_xpath('//div[@class="content"]/div[@class="js-tweet-text-container"]/p')
timestamp=browser.find_elements_by_xpath('//span[@class="_timestamp js-short-timestamp "]')
date=browser.find_elements_by_xpath('//span[@class="_timestamp js-short-timestamp "]')
reply=browser.find_elements_by_xpath('//div[@class="content"]//div[@class="stream-item-footer"]/div[@role="group"]/div[contains(@class,"reply")]/button/span/span')
reply=[i.text for i in reply]
retweet=browser.find_elements_by_xpath('//div[@class="content"]//div[@class="stream-item-footer"]/div[@role="group"]/div[contains(@class,"retweet")]/button/span/span')
retweet=[retweet[i].text for i in [2*i for i in range(int(len(retweet)/2))]]
favorite=browser.find_elements_by_xpath('//div[@class="content"]//div[@class="stream-item-footer"]/div[@role="group"]/div[contains(@class,"favorite")]/button/span/span')
favorite=[favorite[i].text for i in [2*i for i in range(int(len(favorite)/2))]]
#评论所在网站
button=browser.find_elements_by_xpath('//div[@class="content"]/div[@class="stream-item-header"]/small[@class="time"]/a')
comments_urls=[i.get_attribute('href') for i in button]


abstracts=[i.text for i in abstract]
timestamps_s_today=[i.get_attribute('data-time') for i in timestamp_today]
timestamps_ms_today=[i.get_attribute('data-time-ms') for i in timestamp_today]
timestamps_s=[i.get_attribute('data-time') for i in timestamp]
timestamps_ms=[i.get_attribute('data-time-ms') for i in timestamp]



df=pd.DataFrame()
df["abstract"]=abstracts[1:]
df["timestamps_s"]=timestamps_s_today+timestamps_s[1:]
df["timestamps_ms"]=timestamps_ms_today+timestamps_ms[1:]
df["Time"]=df["timestamps_s"].apply(lambda x: time.strftime("%Y/%m/%d %H:%M:%S",time.localtime(int(x))))
df["reply"]=reply[1:]
df["retweet"]=retweet[1:]
df["favorite"]=favorite[1:]
df["comments_urls"]=comments_urls[1:]
print(df)
#df.to_excel("Twitter_vechain_2019_01_08.xlsx")




