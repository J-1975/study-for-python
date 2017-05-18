#!/usr/bin/env python
#coding:utf-8
#Date:20170510
#Author:1975

from bs4 import BeautifulSoup
import urllib2,re

class Region(object):
    def __init__(self):
        pass

    #获取商区、菜系、地标、氛围等分类URL
    def region_list(self, url):
        region = []
        try:
            req = urllib2.Request(url)
            res = urllib2.urlopen(req)
            data = res.read()
        except:
            print u'商区、菜系、地标、氛围等分类URL获取失败',
            exit()

        data_soup = BeautifulSoup(data, 'html.parser', from_encoding='utf-8')
        reg_list = data_soup.find_all('script', class_='J_auto-load')
        url_data = reg_list[0].get_text()
        rfilter = re.compile(r"<a href=\"(.+)\" onclick=\"pageTracker._trackPageview")
    
        for l in url_data.split("</a>"):
            l = rfilter.findall(l)
            if len(l) > 0:
                u = 'https://www.dianping.com'+l[0]
                region.append(u)
        return set(region)