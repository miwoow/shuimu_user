#!/bin/env python
#encoding:utf-8

import threading

import urllib2
import lxml.html.soupparser as soupparser
import json
from pymongo import MongoClient

class PageSpider(threading.Thread):
    def __init__(self, startPage, endPage, cookie):
        threading.Thread.__init__(self)
        self.startPage = startPage
        self.endPage = endPage
        self.cookie = cookie
        self.base_url_pat = "http://www.newsmth.net/nForum/online?ajax&p=%d"
        self.client = MongoClient('127.0.0.1', 27017)
        self.db=self.client.shuimu
        self.shuimu_user=self.db.shuimu_user

    def _get_user_info(self, user_id):
        user_info_url = 'http://www.newsmth.net/nForum/user/query/%s.json' % user_id
        req = urllib2.Request(user_info_url)
        req.add_header('X-Requested-With', 'XMLHttpRequest')
        req.add_header('User-Agent', 'Mozilla/5.0 (X11; FreeBSD amd64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36')
        user_content = urllib2.urlopen(req).read().decode('gbk', 'ignore')
        try:
            info = json.loads(user_content)
        except Exception, ex:
            print '%s json load failed.' % user_id
            return
        self.shuimu_user.insert_one(info)
        
    def _get_user_list_from_page(self, url):
        print url
        req = urllib2.Request(url)
        req.add_header('Cookie', self.cookie)
        req.add_header('User-Agent', 'Mozilla/5.0 (X11; FreeBSD amd64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36')
        response = urllib2.urlopen(req)
        content = response.read()
        dom = soupparser.fromstring(content.decode('gbk'))
        unodes = dom.xpath('//tr/td[2]/a')
        for u in unodes:
            self._get_user_info(u.text)
            
    def run(self):
        for i in xrange(self.startPage, self.endPage):
            self._get_user_list_from_page((self.base_url_pat % (i+1)))
