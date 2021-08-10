# -*- coding:utf-8 -*-
"""
Author: Mohan Ren
Date: 08//10//2021//
"""
import requests

if __name__ == "__main__":
    url = 'https://www.baidu.com/s?wd=ip'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 Edg/91.0.864.54"
    }

    page_text = requests.get(url=url, headers=headers, proxies={'htttps':'59.55.166.183'}).text

    with open("ip.html", 'w', encoding='utf-8') as fp:
        fp.write(page_text)