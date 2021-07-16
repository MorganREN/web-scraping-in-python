# -*- coding:utf-8 -*-
"""
Author: Mohan Ren
Date: 07//16//2021//
"""
import requests
from lxml import html

if __name__ == "__main__":
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 Edg/91.0.864.54"
    }
    url = "https://sc.chinaz.com/ppt/free.html"

    # requests得到html文本
    page_text = requests.get(url=url, headers=headers).text

    # 实例化etree对象
    etree = html.etree
    tree = etree.HTML(page_text)
    # print(tree)
    # 主页操作
    div_top_list = tree.xpath("/html/body/div[3]/div[4]/div")
    # 由于body内的第一个第一个div的display为none，违反 HTML 中已经定义的显示层次结构,因此本排在第四位的div
    # 变成了第三位。 因此注意此后style设置display的要求

    for div_top in div_top_list:
        href = div_top.xpath("./div[2]/a/@href")[0]
        detail_url = "https://sc.chinaz.com" + href
        # print(detail_url)
        # 开始对具体的某一模板进行操作，提取出其下载的url
        detail_page_text = requests.get(url=detail_url, headers=headers).text
        tree_ex = etree.HTML(detail_page_text)
        href = tree_ex.xpath("/html/body/div[4]/div[1]/div[4]/div[2]/div[1]/a[1]/@href")[0]
        print(href)

    # 持久化保存不再继续