# -*- coding:utf-8 -*-
"""
Author: Mohan Ren
Date: 07//06//2021//
"""
# 需求：爬取58二手房中的房源信息
from lxml import html
import requests
from lxml import html

if __name__ == "__main__":
    # 爬取到页面源码数据
    url = "https://bj.58.com/ershoufang/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 Edg/91.0.864.54"
    }
    page_text = requests.get(url=url, headers=headers).text

    # 数据解析
    etree = html.etree
    tree = etree.HTML(page_text)
    div_list = tree.xpath('body/div[@id="__nuxt"]/div[@id="__layout"]/div[@class="list"]/section[@class="list-body"]/section[@class="list-main"]/section[@class="list-left"]/section[@class="list"]/div')
    print("Hello")
    for div in div_list:
        # title = div.xpath('./a[@class="property-ex"]/@href') # 抓取链接
        title = div.xpath('./a[@class="property-ex"]//text()') # 抓取文字
        print(title)
    