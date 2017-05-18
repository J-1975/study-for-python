#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Author: 1975

def func1(arg1,arg2):
	return arg1 == arg2

print dir(func1.__code__)

print func1.__code__.co_varnames

print func1.__code__.co_filename

'''
函数变量的作用域
python代码执行顺序从上往下
'''
global arg
arg = 1

def func2():
	global arg
	arg = 2

def func3():
	global arg
	arg = 3

func3()
#func2()

print arg

'''
函数中引入可变参数(如list支持自修改)如果在函数中对值进行了修改，会导致引入的可变参数本身的值也被修改
'''

def func4(arg):
	arg[0] = 233
	return arg

tlist = [1,2,3,4,5,6,7]

print func4(tlist)
print tlist

'''
定义一个方法get_cjsum(),求1-100范围内的所有整数的平方和。返回结果为整数类型
1.最外层一个while1-100
2.求整数的平方和，累加

'''
def get_cjsum(snum):
	x = 1
	number_sum = 0
	xx = 0
	while (x <= snum):
		#平方值
		xx = x*x
		#平方和累加
		number_sum += xx
		if x == snum:
			return number_sum
		x += 1
assert type(get_cjsum(10)) == int
print get_cjsum(10)