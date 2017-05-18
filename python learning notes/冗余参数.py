#!/usr/bin/env python
#-*- encoding: utf-8 -*-
#Author: 1975
#date: 20170302

def t1(x,y):
    print "x: "+x,"y: "+y
tt1 = ('233','666')
t1(*tt1)
#--------------------------------------#
print u'键名对应传参'
def t2(name="bob",sex=1):
    print "name: %s" % name,"sex: %s" % sex
tt2 = ('luola','0')
tt21 = {'sex':'007','name':'nb'}
t2(*tt2)
t2(**tt21)
#--------------------------------------#
print u'处理传入多余的参数'
def t3(x,*args):
    print "x: %s" % x
    print args
tt3= ('xe2xx',23,14,32,45,254,4,5,45,4,'sdf','wef2',232)
t3(*tt3)
#--------------------------------------#

def t4(y,*args,**kwargs):
    print "x: %s" % y
    print args
    print kwargs
t4('xyz','wr3r','wef',4,123,name='654',love='me')
#--------------------------------------#