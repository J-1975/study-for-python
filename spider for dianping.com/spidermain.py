#!/usr/bin/env python
#coding:utf-8
#Date:20170510
#Author:1975

import excelwt, dataget, urls, region

class dianping(object):
    def __init__(self):
        self.req = dataget.Data()
        self.ewt = excelwt.DataSave()
        self.sid = urls.ShopId()
        self.reg = region.Region()

    #格式化写入excel表的数据
    def data_format(self, uid):
    	row = []
        price,info = self.req.get_price(uid)
        traninfo,bhours = self.req.businessHours(uid)
        tuan,wai = self.req.group_out(uid)
        #print price, info, traninfo, bhours, tuan, wai
        traninfo = '|'.join(traninfo)
        fc = "%s\%s\%s\%s" % (wai, tuan, traninfo, bhours)
        row = {0:price, 1:info[0], 2:info[1], 3:info[2], 4:fc}
        return row

    #利用差集去用重
    def dset(self, ls):
        shopids = []
        new_ls = list(set(ls).difference(set(shopids)))
        shopids.extend(new_ls)
        return new_ls

if __name__ == '__main__':
    rows = 1
    root_url = 'https://www.dianping.com/changchun/food'
    craw = dianping()
    reg_url = craw.reg.region_list(root_url)
    wbook,wsheet,style = craw.ewt.wt()
    #uid = ['2315611', '76678586']
    for ru in reg_url:
        print '*' * 17+u'抓取信息'+'*' * 17
        print u'当前大类URL：'+ru

        shopid = craw.sid.sid(ru)
        shopid = craw.dset(shopid)
        print '^' * 7+u'此大类下所有的店铺id'+'^' * 7
        print shopid
        
        #rows = 1
        for x in set(shopid):
            print u'正在抓取信息的店铺id：'+x
            nrow = craw.data_format(x)
            for c in xrange(5):
                wsheet.write(rows, c, nrow[c], style)
            rows += 1
        print u'已抓取并保存的信息条数：'+str(rows)+"\n\n\n"
        wbook.save('test.xls')
