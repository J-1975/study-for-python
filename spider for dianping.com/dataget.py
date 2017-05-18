#!/usr/bin/env python
#coding:utf-8
#Date:20170510
#Author:1975

import urllib2,json

class Data(object):
    def __init__(self):
        pass

    #get_price函数获取并返回人均消费、口味评价、环境评价、服务评价等信息
    def get_price(self, shopid):
        url = 'https://www.dianping.com/ajax/json/shopDynamic/reviewAndStar?shopId='+shopid+'&cityId=9&mainCategoryId=110'
        headers = {
            "Host": "www.dianping.com",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "X-Requested-With": "XMLHttpRequest",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
            "Referer": "https://www.dianping.com/shop/"+shopid,
            "Cookie": "_hc.v=cd155bf5-7489-9510-07ee-f9958ec256c2.1494385498; __utma=1.1716304894.1494385498.1494385498.1494385498.1; __utmb=1.6.10.1494385498; __utmc=1; __utmz=1.1494385498.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; s_ViewType=10; PHOENIX_ID=0a01791f-15bf05708cd-aef9e89; JSESSIONID=79A4E19125D1ACE7BE949FF8B9686A2E; aburl=1; cy=1; cye=shanghai; __mta=122024756.1494385900364.1494385900364.1494385906227.2"
        }

        request = urllib2.Request(url, headers=headers)
        try:
            res = urllib2.urlopen(request)
            data = res.read()
            st = json.loads(data)
        except:
            st = {}
            print u'get_price函数获取的api接口值为空，请人工排查是否为网络问题'

        return st.get('avgPrice', 'None'), st.get('shopRefinedScoreValueList', 'None')

    #businessHours函数获取营业时间、停车位等信息
    def businessHours(self, shopid):
        url = 'https://www.dianping.com/ajax/json/shopfood/wizard/BasicHideInfoAjaxFP?_nr_force=1494388811962&shopId='+shopid
        headers = {
            "Host": "www.dianping.com",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "X-Requested-With": "XMLHttpRequest",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
            "Referer": "https://www.dianping.com/shop/"+shopid,
            "Cookie": "_hc.v=cd155bf5-7489-9510-07ee-f9958ec256c2.1494385498; __utma=1.1716304894.1494385498.1494385498.1494385498.1; __utmb=1.6.10.1494385498; __utmc=1; __utmz=1.1494385498.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; s_ViewType=10; PHOENIX_ID=0a01791f-15bf05708cd-aef9e89; JSESSIONID=79A4E19125D1ACE7BE949FF8B9686A2E; aburl=1; cy=1; cye=shanghai; __mta=122024756.1494385900364.1494385900364.1494385906227.2"
        }
        
        try:
            request = urllib2.Request(url, headers=headers)
            res = urllib2.urlopen(request)
            data = res.read()
            st = json.loads(data)
        except:
            st = {}
            print u'businessHours函数获取的api接口值为空，请人工排查是否为网络问题'
    
        park_space = st.get('msg').get('parkInfo').get('parkReviews', 'None')

        if type(park_space) == list:
            traninfo = [n.get('tranInfo', 'None') for n in park_space]
        else:
            traninfo = "None"
        bhours = st.get('msg').get('shopInfo').get('businessHours', 'None')
    
        return traninfo, bhours

    #group_out函数返回是否可团购、外卖等信息
    def group_out(self, shopid):
        tuan = u'不团购'
        wai = u'不外卖'
        url = 'https://www.dianping.com/ajax/json/shopDynamic/searchPromo?shopId='+shopid+'&power=5&cityId=1&shopType=10'
        headers = {
            "Host": "www.dianping.com",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "X-Requested-With": "XMLHttpRequest",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
            "Referer": "https://www.dianping.com/shop/"+shopid,
            "Cookie": "_hc.v=cd155bf5-7489-9510-07ee-f9958ec256c2.1494385498; __utma=1.1716304894.1494385498.1494385498.1494385498.1; __utmb=1.6.10.1494385498; __utmc=1; __utmz=1.1494385498.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; s_ViewType=10; PHOENIX_ID=0a01791f-15bf05708cd-aef9e89; JSESSIONID=79A4E19125D1ACE7BE949FF8B9686A2E; aburl=1; cy=1; cye=shanghai; __mta=122024756.1494385900364.1494385900364.1494385906227.2"
        }
        
        try:
            request = urllib2.Request(url, headers=headers)
            res = urllib2.urlopen(request)
            data = res.read()
            st = json.loads(data)
        except:
            st = {}
            print u'group_out函数获取的api接口值为空，请人工排查是否为网络问题'
    
        if st.get('tuan'):
            tuan = u'可团购'
        if st.get('wai'):
            wai = u'可外卖'
    
        return tuan, wai


    #dz函数返回是否可提前订座信息，店铺是否存在均返回"本店可在线提前订座"无意义。
    def dz(self, shopid):
        pass
