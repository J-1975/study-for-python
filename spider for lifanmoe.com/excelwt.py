#!/usr/bin/env python
#coding:utf-8
#Date:20170510
#Author:1975

import xlwt

class DataSave(object):
    def __init__(self):
        pass

    #wt函数返回三个参数，创建excel句柄、excel可写对象、excel保存样式
    def wt(self): 
        wbook = xlwt.Workbook()
        wsheet = wbook.add_sheet('test')
        style = xlwt.easyxf('align: vertical center, horizontal center')
        
        root = [u'人均消费', u'口味评价', u'环境评价', u'服务评价', u'(特色)可外卖\可团购\停车场\营业时间']
        for i in xrange(len(root)):
            wsheet.write(0, i, root[i], style)
        return wbook,wsheet,style
        #wbook.save('test.xls')