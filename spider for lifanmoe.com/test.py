#!/usr/bin/env python
#coding:utf-8
#data:20170501

from bs4 import BeautifulSoup
import requests,re,json,sys

reload(sys)
sys.setdefaultencoding('utf-8')

def detail_url(url):
    if url is None:
        return

    url_res = requests.get(url)
    content = url_res.text

    url_soup = BeautifulSoup(content, 'html.parser', from_encoding='utf-8')
    img = url_soup.find_all('div', class_='entry-content content-reset')
    img = img[0].find_all('img',src=re.compile(r"(.+)"))
    #print 'https://'+img['src'].split('//')
    for i in img:
        if len(img) > 0:
            i = 'https://'+i['src'].split('//')[1]
            img_content = requests.get(i)
            with open(i.split('/')[-1],'wb') as name:
                name.write(img_content.content)
            name.close()

detail_url('https://lifanmoe.com/meitu/gif/8164/')
