#!/bin/env python
#encoding:utf-8


from PageSpider import PageSpider


if __name__ == "__main__":
    base = 0
    ths = []
    # TODO: set your cookie.
    cookie = 'main[UTMPUSERID]=liamxd; main[UTMPKEY]=63945138; main[UTMPNUM]=4953; main[PASSWORD]=%2509%257BKb3A%2503%2513%2505%2501%250DR%251BF%2506%2504%2524u%2511%2506%250Eu__; smth_float=true; left-index=00000000010; main[XWJOKE]=hoho; nforum-left=00010; Hm_lvt_9c7f4d9b7c00cb5aba2c637c64a41567=1438590956,1438653416,1438664277,1439171647; Hm_lpvt_9c7f4d9b7c00cb5aba2c637c64a41567=1439172490; bfd_s=88525828.51719388.1439171647440; tmc=13.88525828.79838948.1439171647445.1439172070507.1439172490461; tma=88525828.24801104.1436576277002.1438653415818.1439171647454.5; tmd=80.88525828.24801104.1436576277002.; bfd_g=8a7bc81f66bd068d00004c9400031d7d55a068fd'
    for i in xrange(10):
        ths.append(PageSpider(base, base+101, cookie))
        base += 100
    for i in ths:
        i.start()
    for i in ths:
        i.join()
    print '[INFO] Done.'
        
        



