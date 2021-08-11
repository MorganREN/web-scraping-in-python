# -*- coding:utf-8 -*-
"""
Author: Mohan Ren
Date: 08//11//2021//
"""
import requests

headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 Edg/91.0.864.54"
    }

def get_content(url):
    print('正在爬取: ', url)
    response = requests.get(url=url, headers=headers) # get方法是一个阻塞的方法
    if response.status_code == 200:
        return response.content

def parse_content(content):
    print("响应数据长度为: ", len(content))

if __name__ == "__main__":
    urls = {
        'http://xmdx.sc.chinaz.net/Files/DownLoad/jianli/201904/jianli10231.rar',
        'http://zjlt.sc.chinaz.net/Files/DownLoad/jianli/201904/jianli10229.rar',
        'http://xmdx.sc.chinaz.net/Files/DownLoad/jianli/201904/jianli10231.rar'
    }
    for url in urls:
        content = get_content(url)
        parse_content(content)