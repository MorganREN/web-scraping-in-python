# -*- coding:utf-8 -*-
"""
Author: Mohan Ren
Date: 08//13//2021//
"""
import requests
import asyncio
import time
# 使用该模块中的ClientSession对象
import aiohttp

start = time.time()
urls = [
    'http://127.0.0.1:5000/bobo',
    'http://127.0.0.1:5000/jay',
    'http://127.0.0.1:5000/mohan'
]

async def get_page(url):
    async with aiohttp.ClientSession() as session:
        # get()/post():
        # headers,params/data,proxy='http://ip:prot'
        async with await session.get(url) as response:
            # text()返回字符串形式的响应数据
            # read()返回二进制形式的响应数据
            # json()返回的就是json对象
            page_text = await response.text() # 注意：在获取响应数据操作之前，一定要使用await进行手动挂起
            print(page_text)

tasks = []

for url in urls:
    c = get_page(url)
    task = asyncio.ensure_future(c)
    tasks.append(task)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

print('time spent: ',time.time()-start)