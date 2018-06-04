#!/usr/bin/env python
# coding=utf-8

import urllib3, time, os
from apscheduler.schedulers.blocking import BlockingScheduler

pool = urllib3.PoolManager()


# 2018年五一假期五折券
def getquan():
    i = 100
    while True:
        i = i - 1
        if i < 0:
            break
        else:
            resp = pool.request('POST', 'http://mktm.zuche.com/weika/getQuan.do?'
                                        'mobile=18701685341&szhdbm=&from=mdfdiscount')
            res_data = resp.data.decode('utf-8')
            print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()), resp.status, res_data)
            time.sleep(0.2)


# 2018年端午假期五折券
def getquan2():
    i = 100
    while True:
        i = i - 1
        if i < 0:
            break
        else:
            resp = pool.request('POST', 'http://mktm.zuche.com/weika/getQuan.do?'
                                        'mobile=18710035834&szhdbm=&from=msduanwu')
            res_data = resp.data.decode('utf-8')
            print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()), resp.status, res_data)
            time.sleep(0.5)


if __name__ == "__main__":
    sched = BlockingScheduler()
    sched.add_job(getquan2, trigger="cron", hour=13, minute=59, second=30)
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
    try:
        sched.start()
    except (KeyboardInterrupt, SystemExit):
        sched.shutdown()
        print('Exit The Job!')
