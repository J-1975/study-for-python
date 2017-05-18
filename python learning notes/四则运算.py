#!/usr/bin/env python
#-*- encoding: utf-8 -*-
#Author: 1975
#date: 20170302
import sys
'''
四则运算脚本
'''
ys = sys.argv[2]
value1 = int(sys.argv[1])
value2 = int(sys.argv[3])
if ys == '+':
  print value1+value2
elif ys == '-':
  print value1-value2
elif ys == '*':
  print value1*value2
elif ys == '/':
  print value1/value2
else:
  print u'此脚本只能进行四则运算！\nExample:test.py 1 * 3'
