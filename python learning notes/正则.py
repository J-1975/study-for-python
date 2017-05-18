#!/usr/bin/env python
#coding:utf-8
#data:200170418

import re
st1 = "top tip test tqp tep ttt"
se1 = r"t[^io]p"	#匹配字符串t开头p结尾，中间不包含有i或者o的字符串
#print re.findall(se1,st1)

st = "123 ewq 12345566 123qwe 233 6666 123qwe"
#sea = r"^233" #匹配字符串开头是否有233
sea = r"qwe$"	#匹配行尾
#print re.findall(sea,st)

st2 = "^abc"
sea2 = r"\^abc"
#print re.findall(sea2,st2)

#print "123 +\r+ qwe +\n+ 233 +\t+ 666 +\v+ 123qwe +\f+"

st3 = "010-12345678"
sea3 = r"^010-\d{8}"	#匹配010-开头的后面位数为8位的电话
#print re.findall(sea3,st3)

st4 = "abbbbbbbbbbc23233123qw6661234567890987654321sdfag"
sea4 = r"[ab3]*"	#把*号前面的字符串至少出现0次或者多次，0次就是没有
#print re.findall(sea4,st4)

st5 = "abbbbbbbbbbc23233123qw6661234567890987654321sdfag"
sea5 = r"[abx]+"	#把+号前面的字符串至少出现1次或者多次
#print re.findall(sea5,st5)

sea6 = r"^010-?\d{8}$"	#匹配010开头，后8位数的电话，符号"-"可出现0次或1次
#print re.findall(sea6,"010-12345678")

#print re.findall(r"ab+?","abbbbbbbb")	#非贪婪模式匹配
#print re.findall(r"ab*","abbbbbbbb")	#贪婪模式匹配
#print re.findall(r"ab{1,3}","abbbbbbbbbbbbb")	#{m,n}至少匹配m次，至多匹配n次；{0,}等同于*，{1,}等同于+，{0,1}等同于?

com = re.compile(r"InFo",re.I)	#不区分大小写匹配
#print com.findall("infO")

#match()匹配字符在开头，匹配到则成功返回一个对象，失败则没有返回，可用group()返回match匹配到的对象
#search()搜索整个字符串进行匹配，匹配到则成功返回一个对象，失败则没有返回

rs = r"c..v"	#一位小数点代表一个字符
#print re.sub(rs,"test","ccav cctv cccc cqav coav")
#print re.subn(rs,"test","ccav cctv cccc cqav coav")

'''
re.S 匹配\t \n等
re.I 不区分大小写匹配
re.M 多行匹配，如多行数据存到一个变量中换行符等用\n\r代替了，这是要匹配需要用到re.M
re.X 正则中多行匹配
'''
#print re.findall(r"csvt.net","csvt\nnet",re.S)		#加上re.S可以匹配空格换行符等
st7 = """
123 qwe 34
233werwerwd dfsf 
66e erwrw
23333
"""
#print re.findall(r"^233",st7,re.M)

sea7 = r"""
\d{3,4}
-?
\d{8}
"""
#print re.findall(sea7,"010-12345678",re.X)

email = r"\w{3}@\w+(\.com|\.cn)"
#print re.findall(email,"zzz@qwe.com")	#在有分组的情况下，findall会优先返回分组当中的数据

s = """
sdfsdf 123 src=qweqwds ooo sdfwewmfedfdf d d
 src=8io90
 sadasd sdfsdf 123 src=rfv ooo qweq
sdf 12e3fd 123 src=5tgb ooo
"""
r = r"123 src=(.+) ooo"	#优先返回分组中的数据
print re.findall(r,s)