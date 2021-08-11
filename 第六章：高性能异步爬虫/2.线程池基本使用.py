# -*- coding:utf-8 -*-
"""
Author: Mohan Ren
Date: 08//11//2021//
"""

'''
import time
#使用单线程串行方式执行
def get_page(str):
    print("Downloading: ", str)
    time.sleep(2)
    print("Done: ", str)
    time.sleep(0.2)

if __name__ == "__main__":
    name_list = ['xiaozi', 'aa', 'bb', 'cc']

    start_time = time.time()
    for i in range(len(name_list)):
        get_page(name_list[i])

    end_time = time.time()
    print('%d second'% (end_time-start_time))'''

import time
from multiprocessing.dummy import Pool # 导入线程池模块对应的类
#使用线程池方式执行

def get_page(str):
    print("Downloading: ", str)
    time.sleep(2)
    print("Done: ", str)

if __name__ == "__main__":
    start_time = time.time()
    name_list = ['xiaozi', 'aa', 'bb', 'cc']
    pool = Pool(4)  # 实例化一个线程池对象，参数4说明有4个线程对象
    pool.map(get_page, name_list)  # 将列表name_list中的每一个元素交给get_page进行处理
    end_time = time.time()
    print(end_time-start_time)

