#!/usr/bin/env python
#-*- coding: utf-8 -*-
#python study

import urllib
import os
import glob
"""
上一节的习题解决

1.习题发生的问题总结
	（1）别管那么多复杂的，先直接把功能实现
	（2）自己要测试。多测试，要完整。
	（3）将函数变得更健壮，让它可以跑很多地方
		功能完善
		异常处理完善

"""

'''
定义一个方法get_num(num),num参数是列表类型，判断列表里面的元素为数字类型。其他类型则报错，并且返回一个偶数列表：（注：列表里

面的元素为偶数）

1.对传入的参数进行类型判断
2.遍历传入的参数是否为数字，不是报错，是则进行下一步；判断是否为偶数，是则加入一个新的列表，不是进行下一步
'''
def get_list(tlist):
	#定义一个空数组
	arg = []
	#遍历数组中的值是否存在非整数值
	for i in tlist:
		if not (isinstance(i,int) or isinstance(i,long)):
			return u'列表参数中存在非数字类型值'
	#m = i%2
	#将偶数添加到定义的数组中去
		if i%2 == 0:
			arg.append(i)
	return arg

print get_list([1,2,34,333,5,66,234,45,234,252,12312312313131312231,2333333333333333333333332])


'''
定义一个方法get_page(url),url参数是需要获取网页内容的网址，返回网页的内容。提示（可以了解python的

urllib模块）

1.对传入的url参数进行连接，判断主机是否存活
2.判断主机响应状态吗是否为200
3.对返回的网页内容进行过滤，获取需要的部分
'''
def get_page(url):
	#获取网站的响应状态码
	rs = urllib.urlopen(url).code
	#判断网站是否正常响应
	if not rs == 200:
		u"网站状态码不为200，获取内容出错"
	#请求网站
	x = urllib.urlopen(url)
	#读取内容
	m = x.read()
	x.close()
	return m
#print get_page('https://www.baidu.com/img/')


'''
定义一个方法get_dir(f),f参数为任意一个磁盘路径，该函数返回路径下的所有文件夹组成的列表，如果没有文件夹则返回"Not dir"
1.判断给定路径是否存在
2.获取文件夹目录，并返回列表

'''
def get_dir(file_path):
	#判断文件夹是否存在
	if not os.path.isdir(file_path):
		print u"文件夹不存在或不能识别"
	#遍历获取的值，并对每一个进行是否为文件夹判断
	for fd in os.listdir(file_path):
		if os.path.isdir("e:/"+fd):
			print fd

get_dir("e:/")