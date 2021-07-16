# -*- coding:utf-8 -*-
"""
Author: Mohan Ren
Date: 07//16//2021//
"""
# 项目需求： 解析出所有城市名称 https://www.aqistudy.cn/historydata/
import requests
from lxml import html

if __name__ == "__main__":
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 Edg/91.0.864.54"
    }
    url = "https://www.aqistudy.cn/historydata/"

    etree = html.etree
    page_text = requests.get(url=url, headers=headers).text
    tree = etree.HTML(page_text)

    ul_list = tree.xpath("/html/body/div[3]/div/div[1]/div[2]/div[2]/ul")
    print(ul_list)
    for ul in ul_list:
        li_list = ul.xpath("./div[2]/li")
        for li in li_list:
            city_name = li.xpath("./a/text()")[0]
            # print(city_name)


