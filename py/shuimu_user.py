#!/bin/env python
#encoding:utf-8

import urllib2
import lxml.html.soupparser as soupparser
import json
from pymongo import MongoClient
import threading
from PageSpider import PageSpider


if __name__ == "__main__":
    base = 0
    ths = []
    for i in xrange(10):
        ths.append(PageSpider(base, base+101))
        base += 100
    for i in ths:
        i.start()
    for i in ths:
        i.join()
    print '[INFO] Done.'
        
        



