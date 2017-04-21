#!/usr/bin/env python
#coding:utf-8
#data:20170420
#Author:1975
'''
简易图片爬虫，获取网站中的美图
①访问目标URL，获取分类目录、页数、详情页连接，创建分类目录
②访问详情页获，取图片链接，筛选匹配出图片URL
③依次遍历并下载保存
'''

import requests,re,os,sys

current_dir = os.getcwd()

#需要获取的图片系列及名称
def img_classification(domain):
    n = ["xingge","rufang","meitui","qingqu","bijini","zhifu","siwa","qunzhuang","av","mote","tpzp","nvyou","xinggan","meinv"]  #设置需要获取的系列
    img_class_list_1 = {}
    get_req = requests.get(domain)
    get_res = get_req.text
    img_class_filter = re.compile(r"<a href=\"(.+)\">(.+)</a>") #正则过滤需要获取的URL和名称
    img_class_list = img_class_filter.findall(get_res)
    img_class_list = list(set(img_class_list))  #去重
    img_class_list = dict(img_class_list)
    for x in n:
        for i in img_class_list.keys():
            if (i.split("/")[1] == x) and (i[-1] == "/") and (len(i.split("/")[2]) > 0):    #根据设置的需要获取的系列来进行筛选
                k = domain+i    #根据获取的URL与域名进行拼接
                v = img_class_list[i]
                img_class_list_1[k]= v
    return img_class_list_1

#页码url及页数获取
def img_page_get(img_p):
    get_req = requests.get(img_p)
    get_res = get_req.text
    img_page_filter = re.compile(r"(\d{1,2})</a> <a class=\"next\" href=\"(.+)\">")
    img_pages = img_page_filter.findall(get_res)
    return img_pages

#每页图片系列URL获取
def img_list_get(img_p,img_u,page):
    img_l = []
    target = []
    for num in range(1,page+1):
        page_url = list(img_u)  #使页码url变为一个list
        page_url[-6] = str(num) #更改页码
        img_pl = ''.join(page_url)
        get_req = requests.get(img_p+img_pl)
        get_res = get_req.text
        img_list_filter = re.compile(r"<a href=\"(.+)html\">")
        img_list = img_list_filter.findall(get_res)
        img_list = [img_p+u.replace(".",".html") for u in img_list]
        img_l += img_list
    return img_l

#单个系列图片url获取函数
def get_img_html(target):
    img_group = []
    for tg in target:
        get_req = requests.get(tg)
        get_res = get_req.text
        img_url_filter = re.compile(r"<img src=\"(.+)\" />")    #第一次图片url过滤规则
        img_list = img_url_filter.findall(get_res)
        filename = tg.split("/")[-1].split(".")[0]  #每一组图片新建一文件夹文件名获取
        img_group += img_list,filename
    return img_group

#图片保存函数
def save_imgs(_img,_file,img_cfile):
    global current_dir
    img_dir = current_dir+"\\"+img_cfile+"\\"+_file #获取当前物理路径并拼接
    if os.path.exists(img_dir) or os.path.isdir(img_dir):   #判断文件夹/同名文件是否存在
        print "file or dir name exists! -->> imgages"
        exit()
    else:
        create_dir = os.makedirs(img_dir)   #建立新的文件夹
        os.chdir(img_dir)   #改变文件路径
    for ix in _img:
        img = ix[:ix.find(",c_fill,")]+".jpg"   #根据之前获取的图片url，进行二次过滤拼接获取高清的图片URL
        img_content = requests.get(img) #请求图片
        with open(img.split("/")[-1],"wb") as source:   #下载并保存图片，图片命名获取图片URL后缀
            source.write(img_content.content)


host = "http://www.ivrfans.cn"  #url
img_class = img_classification(host)
print u"创建分类目录..."
for key in img_class:
    img_cdir = current_dir+"\\"+img_class[key]
    if os.path.isdir(img_cdir) or os.path.isdir(img_cdir):
        print "file or dir name exists! -->> img_class\r"
        print u"网站页面获取的分类目录名重复..."
    else:
        create_dir = os.makedirs(img_cdir)  #给所有分类建立文件夹
for img_tg in img_class:
    par = img_page_get(img_tg)
    if not (len(par) > 0):  #页码小于2将不能获取，par的值将为空
        print u"页码小于或等于1，放弃抓取。"
        continue
    img_u = par[0][1]
    pages = int(par[0][0])
    list_img = img_list_get(host,img_u,pages)
    u_list = get_img_html(list_img)
    u = 0   #每个图片URL的下标
    f = 1   #每一组图片的文件名下标
    num = len(u_list)
    print u,f,num
    while not ((u >= num-1) or (f >= num-1)):
        print u"u=%s,当前分类目录为 %s ..." % (u,img_class[img_tg])
        print u"f=%s,正在抓取的图片目录名 %s ..." % (f,u_list[f])
        save_imgs(u_list[u],u_list[f],img_class[img_tg])
        u += 2
        f += 2
