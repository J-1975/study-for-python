#!/usr/bin/env python
#coding:utf-8
#data:20170501
#Author:1975

from bs4 import BeautifulSoup
import requests

class Shtml(object):
    def __init__(self):
    	pass
    #获取每页中单个系列的URL
    def get_urls(self,_url):
        links = {}
        if _url is None:
            return
    
        res = requests.get(_url)
        content = res.text
    
        page_soup = BeautifulSoup(content, 'html.parser', from_encoding='utf-8')
        #pages_url = page_soup.find_all('option')
        link = page_soup.find_all('a', class_='post-title')
        for l in link:
            links[l['href']] = l.get_text()
        return links
    #获取页数
    def get_pages(self,_page):
        pages = []
        if _page is None:
            return
    
        res = requests.get(_page)
        content = res.text

        page_soup = BeautifulSoup(content, 'html.parser', from_encoding='utf-8')
        pages_url = page_soup.find_all('option')
        for p in pages_url:
            pages.append(p['value'])
        return pages