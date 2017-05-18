#!/usr/bin/env python
#coding:utf-8
#data:20170501

from bs4 import BeautifulSoup
import requests,re,json,sys

reload(sys)
sys.setdefaultencoding('utf-8')

class Img_down(object):
    def __init__(self):
        pass

    def detail_url(self,url):
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
    
    def download_url(self,pid):
        if pid is None:
            return
    
        url = 'https://lifanmoe.com/wp-admin/admin-ajax.php?action=0b673645b61e8dd970bfeaf862543742&52a6ad6bbcc3284915dc7640b01fbd63%5Btype%5D=getUnreadUsers&1029fefda5d2ec72d73091097501565a%5Btype%5D=checkUnread&f490e90094f2dee66cd9c394ab187fea%5Btype%5D=checkSigned&ee0b362e07ca07939cd53ad823b52517%5BpostId%5D=8180&dff90d2506b5ca39c86b3b676fbe2acd%5Btype%5D=getStorage&dff90d2506b5ca39c86b3b676fbe2acd%5Bid%5D='+pid+'&c3ceca030a383001aefb646134cb86c6%5Btype%5D=getItems&c3ceca030a383001aefb646134cb86c6%5BpostId%5D=8180'
        headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        'Accept': '*/*',
        'Referer': 'https://lifanmoe.com/download/?id='+pid,
        'Accept-Encoding': 'gzip, deflate, sdch, br',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Cookie': '__cfduid=d97453705914e61198d2c06ddca5aec0c1493686774; UM_distinctid=15bc6ab4fed7d3-07050717efd5a2-6a11157a-1fa400-15bc6ab4fee4e8; postApprovalId[11754]=1; postApprovalId[11620]=1; postApprovalId[10914]=1; postApprovalId['+pid+']=1; CNZZDATA1255833541=312548314-1493685503-%7C1493690953'}
    
        down_res = requests.get(url,headers=headers)
        content = down_res.text
        data = json.loads(content)
        #return data
        for i in data['customPostStorage']['items']:
            if len(i) > 0:
                with open('download.txt','wb') as file_:
                    file_.write(i.get('name','download url: ')+i.get('url','no url!')+'   downloadPwd: '+i.get('downloadPwd','no downloadPwd!')+'   extractPwd: '+i.get('extractPwd','no extractPwd!')+'\n')
                file_.close()

