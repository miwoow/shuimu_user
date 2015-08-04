#!/bin/env python
#encoding:utf-8


from PageSpider import PageSpider


if __name__ == "__main__":
    base = 0
    ths = []
    # TODO: set your cookie.
    cookie = ''
    for i in xrange(10):
        ths.append(PageSpider(base, base+101, cookie))
        base += 100
    for i in ths:
        i.start()
    for i in ths:
        i.join()
    print '[INFO] Done.'
        
        



