# -*- coding:utf-8 -*-
"""
Author: Mohan Ren
Date: 08//13//2021//
"""
import requests
import asyncio
import time
start = time.time()
urls = [
    'http://127.0.0.1:5000/bobo',
    'http://127.0.0.1:5000/jay',
    'http://127.0.0.1:5000/mohan'
]

async def get_page(url):
    print("Downloading ", url)
    # request.get是基于同步，必须使用基于异步的网络请求模块进行指定url的请求发送
    # aiohttp: 基于异步网络请求的模块
    response = requests.get(url=url)
    print('Done: ', response.text)

tasks = []

for url in urls:
    c = get_page(url)
    task = asyncio.ensure_future(c)
    tasks.append(task)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

print('time spent: ',time.time()-start)