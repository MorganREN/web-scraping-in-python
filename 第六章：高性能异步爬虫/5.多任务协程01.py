# -*- coding:utf-8 -*-
"""
Author: Mohan Ren
Date: 08//13//2021//
"""
import asyncio
import time

async def requests(url):
    print("Downloading", url)
    # time.sleep(2) # 在异步协程中如果出现了同步模块相关的代码，那么就无法实现异步。
    # 当在asycio中遇到阻塞操作，必须进行手动挂起
    await asyncio.sleep(2)
    print('Finished', url)
start = time.time()
urls = [
    'www.baidu.com',
    'www.sogou.com',
    'www.alibaba.com'
]

# 任务列表：存放多个任务对象
tasks = []
for url in urls:
    c = requests(url)
    task = asyncio.ensure_future(c)
    tasks.append(task)

loop = asyncio.get_event_loop()
# 需要将任务列表封装到wait中
loop.run_until_complete(asyncio.wait(tasks))
print(time.time()-start)