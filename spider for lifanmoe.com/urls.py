#!/usr/bin/env python
#coding:utf-8
#data:20170515
#Author:1975

from bs4 import BeautifulSoup
from StringIO import StringIO
import urllib2,re,gzip

class ShopId(object):
    def __init__(self):
        pass

    #接收一个url，发起http请求并处理gzip压缩过的网页内容
    def single_list(self, url):
        host = 'https://www.dianping.com'
        headers = {
        "Host": "www.dianping.com",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Referer": "https://www.dianping.com/changchun/food",
        "Accept-Encoding": "gzip, deflate, sdch, br",
        "Accept-Language": "zh-CN,zh;q=0.8",
        "Cookie": "_hc.v=52e82e2a-e948-b73f-29ef-09315990bf48.1494773109; __utma=1.1188402881.1494773109.1494773109.1494773109.1; __utmb=1.3.10.1494773109; __utmc=1; __utmz=1.1494773109.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __mta=246240827.1494773128205.1494773128205.1494773128205.1; JSESSIONID=536A06B8E3C5F9D0DEC2C699B6D4D194; aburl=1; cy=70; cye=changchun; PHOENIX_ID=0a010444-15c076c86a4-c9685c7"
        }
        
        try:
            req = urllib2.Request(url, headers=headers)
            res = urllib2.urlopen(req)
            #处理gzip压缩过的网页内容
            buf = StringIO( res.read())
            f = gzip.GzipFile(fileobj=buf)
            data = f.read()
        except:
            data = ""
        return data
    
    #处理html内容，返回页码数
    def pages(self, html_data):
        pages = []
        data_soup = BeautifulSoup(html_data, 'html.parser', from_encoding='utf-8')
        page = data_soup.find_all('a', class_="PageLink")
        for p in page:
            pages.append('https://www.dianping.com'+p['href'])
        return pages
    
    #处理html内容，返回店铺id列表
    def url_list(self, html_data):
        u_list = []
        data_soup = BeautifulSoup(html_data, 'html.parser', from_encoding='utf-8')
        sin_list = data_soup.find_all('a', onclick=re.compile(r"document(.+)"))
        for u in sin_list:
            u_list.append(u['href'].split('/')[-1])
        return u_list
    
    def sid(self, url):
        sid = []
        data_new = self.single_list(url)
        if len(data_new) < 0:
            return
        pages_new = self.pages(data_new)
        pages_new.append(url)
        for pn in pages_new:
            sid.extend(self.url_list(self.single_list(pn)))
        return sid
