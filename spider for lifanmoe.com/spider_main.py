#!/usr/bin/env python
#coding:utf-8
#data:20170502
#Author:1975

import img_downurl,htmlparser,url_lists,os

class SpiderMain(object):
    def __init__(self):
        self.dirs = url_lists.Furl()
        self.urls = htmlparser.Shtml()
        self.imgs = img_downurl.Img_down()

    def dir_url(self,root_url):
        dir_lists = craw.dirs.class_url(root_url)

        dir_dict = {}
        for dl in dir_lists:
            if ('yinyue' in dl['href']) or ('youxi' in dl['href']):
                pass
            else:
                dir_dict[dl['href']] = dl.get_text()
        return dir_dict

    def pages_url(self,dir_url):
        urls = []
        for url in dir_url:
            pages = self.urls.get_pages(url)
            for u in pages:
                if u in urls:
                    continue
                urls.append(u)
                print u'正在读取分类%s下的%s页码..' % (dir_url[url],u)
                detail = craw.urls.get_urls(u)
                for k in detail:
                    pid = k.split('/')[-2]
                    pid_dir = path_pwd+'/'+dir_url[url]+'/'+pid
                    os.makedirs(pid_dir)
                    os.chdir(pid_dir)
                    try:
                        craw.imgs.detail_url(k)
                        print detail[k]+u'已采集..'
                        craw.imgs.download_url(pid)
                    except:
                        print u'连接错误!%s' % k
        #return urls


if __name__ == '__main__':
    path_pwd = os.path.dirname(os.getcwd())
    root = 'https://lifanmoe.com'
    craw = SpiderMain()
    dlist = craw.dir_url(root)
    for dirs in dlist:
        c_path = path_pwd+'/'+dlist[dirs]
        if os.path.exists(c_path) or os.path.isdir(c_path):
            print u'分类目录%s已存在..' % dlist[dirs]
        else:
            os.makedirs(c_path)
            print u'分类目录',dlist[dirs],'已建立..'
    craw.pages_url(dlist)

