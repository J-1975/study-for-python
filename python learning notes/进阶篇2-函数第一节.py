#!/usr/bin/env python
#-*- coding=utf-8 -*-
#python study

import os
import glob

'''
函数相关
*num是一个元祖

函数的参数
1.可选参数 是有默认值的
2.必须参数 是没有默认值的
默认值的区别在与 "="

函数的健壮性
1.你永远知道你的方法会返回什么(异常处理，条件判断)
2.返回你想要的结果


'''

def add(*num):
	u"任意多个整数相加"
	s = 0
	for i in num:
		if isinstance(i,int):
			pass
		else:
			return u'参数中有不是数字的类型'
		s += i
	return s
print u''
print add(1,233,4,5,6,3,424,234,242,2342)

'''
课后习题
'''

def funcmm(*num):
	'定义一个方法 func，该func可以引入任意多的整型参数，结果返回其中最大与最小的值'
	for i in num:
		if not isinstance(i,int):
			return u'参数中有不是数字的值'
	#利用sorted来直接排序
	x = sorted(num)

	return "max number is %d, min number is %d" % (x[-1],x[0])

print u'求最大和最小数 进阶函数-1'
print funcmm(12,23,424,3,5354,34,4,324,2,41343,43,3,33)


def funccd(*zifu):
	'定义一个方法func，该func可以引入任意多的字符串参数，结果返回（长度）最长的字符串'
	for i in zifu:
		if not isinstance(i,str):
			return u'参数值中存在非字符串类型字符'

	x = sorted(zifu,key=lambda z:len(z))

	return "max length string is: %d" % len(x[-1])

print u'返回任意多字符串中长度最长的字符串(长度) 进阶函数-2'
print funccd('123','fewfw','wfwefewefwf1','efw3333','111222333')

def get_doc(module):
	'定义一个方法get_doc(module)，module参数为该脚本中导入或定义的模块对象，该函数返回module的帮助文档'
	a = 'pydoc %s' % module
	m = os.popen(a).read()
	return m

print u'函数返回module的帮助文档 进阶函数-3'
#print get_doc(urllib)


'''
输入文件名，读取其内容
'''
def get_text(f):
	x = 'type %s' % f
	m = os.popen(x).read()
	return m

#print get_text('e:\url.txt')


'''
返回一个文件夹中的文件列表
'''
def get_dir(folder):
	x = "%s/*.*" % folder
	temp = glob.glob(x)
	if temp == []:
		return u"文件夹不存在或为空"
	return temp

print get_dir('E:\python-study')
