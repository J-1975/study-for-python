#!/usr/bin/env python
#coding:utf-8
#data:20170501
#Author:1975

from bs4 import BeautifulSoup
import requests,re

class Furl(object):
    def __init__(self):
    	pass
    #获取需要的分类
    def class_url(self,host):    
        if host is None:
            return
    
        res = requests.get(host)
        content = res.text
    
        host_soup = BeautifulSoup(content, 'html.parser', from_encoding='utf-8')
        dir_urls = set(host_soup.find_all('a', href=re.compile(r'https://lifanmoe.com/category/(\w{2,7}/)')))
        return dir_urls

#u = 'https://lifanmoe.com/'
#test = Furl()
#print test.class_url(u)
