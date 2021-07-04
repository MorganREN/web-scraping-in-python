# -*- coding:utf-8 -*-
"""
Author: Mohan Ren
Date: 06//29//2021//
"""

# UA：User-Agent（请求载体的身份标识）
# 反爬机制：UA检测（门户网站的服务器会检测对应请求的载体身份标识，如果检测到请求的载体身份标识为某一款浏览器，
# 说明该请求为一个正常请求。 但是如果请求载体身份标识不是基于某一款的浏览器的，则表示该请求
# 为不正常请求（爬虫），则服务器端就很有可能拒绝该次请求。

# UA伪装：让爬虫对应的请求载体身份标识伪装成某一款浏览器
import requests

if __name__ == "__main__":
    # UA伪装：将对应的User—Agent封装到一个字典中
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 Edg/91.0.864.54"
    }
    url = "https://www.sogou.com/web?"
    # Deal with the parameter in the url: produce a dictionary
    kw = input("Enter the word: ")
    param = {
        "query": kw
    }
    response = requests.get(url=url, params=param, headers = headers)
    page_text = response.text

    fileName = kw + ".html"
    with open(fileName, "w", encoding='utf-8') as fp:
        fp.write(page_text)

    print(fileName, "save finished")