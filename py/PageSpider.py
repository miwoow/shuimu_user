#!/bin/env python
#encoding:utf-8

import threading

global client
global db
global shuimu_user

client = MongoClient('127.0.0.1', 27017)
db=client.shuimu
shuimu_user=db.shuimu_user

def _get_user_info(user_id):
    user_info_url = 'http://www.newsmth.net/nForum/user/query/%s.json' % user_id
    req = urllib2.Request(user_info_url)
    req.add_header('X-Requested-With', 'XMLHttpRequest')
    user_content = urllib2.urlopen(req).read().decode('gbk', 'ignore')
    try:
        info = json.loads(user_content)
    except Exception, ex:
        user_content = user_content.replace(',"face_url":', '","face_url":')
        info = json.loads(user_content)
    shuimu_user.insert_one(info)

def _get_user_list_from_page(url):
    print url
    req = urllib2.Request(url)
    req.add_header('Cookie', 'fancy_adclick=preimg/1438664303; main[XWJOKE]=hoho; left-index=10000000000; nforum-left=00010; Hm_lvt_9c7f4d9b7c00cb5aba2c637c64a41567=1438586870,1438590956,1438653416,1438664277; Hm_lpvt_9c7f4d9b7c00cb5aba2c637c64a41567=1438668799; bfd_s=88525828.16390369.1438664277024; tmc=6.88525828.14615510.1438664277029.1438668653627.1438668799034; tma=88525828.24801104.1436576277002.1438568221879.1438653415818.4; tmd=45.88525828.24801104.1436576277002.; bfd_g=8a7bc81f66bd068d00004c9400031d7d55a068fd; NFORUM=f25253ojgeippr8itvhar6mlh4; main[UTMPUSERID]=liamxd; main[UTMPKEY]=73681677; main[UTMPNUM]=5301; main[PASSWORD]=%2509%257BKb3A%2503%2513%2505%2501%250DR%251BF%2506%2504%2524u%2511%2506%250Eu__')
    response = urllib2.urlopen(req)
    content = response.read()
    dom = soupparser.fromstring(content.decode('gbk'))
    unodes = dom.xpath('//tr/td[2]/a')
    for u in unodes:
        _get_user_info(u.text)
        


class PageSpider(threading.Thread):
    def __init__(self, startPage, endPage):
        threading.Thread.__init__(self)
        self.startPage = startPage
        self.endPage = endPage
        self.base_url_pat = "http://www.newsmth.net/nForum/online?ajax&p=%d"

    def run(self):
        for i in xrange(self.startPage, self.endPage):
            _get_user_list_from_page((base_url_pat % (i+1)))
