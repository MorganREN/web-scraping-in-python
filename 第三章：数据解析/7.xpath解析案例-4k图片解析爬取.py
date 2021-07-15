# -*- coding:utf-8 -*-
"""
Author: Mohan Ren
Date: 07//15//2021//
"""

# 需求：解析下载图片数据 https://pic.netbian.com/4kmeinv/

import requests
from lxml import html
import os

if __name__ == "__main__":
    url = "https://pic.netbian.com/4kmeinv/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 Edg/91.0.864.54"
    }
    response = requests.get(url=url, headers=headers)
    # 手动设定响应数据对象的编码格式
    # response.encoding = 'utf-8'
    page_text = response.text

    if not os.path.exists('./meinvLibs'):
        os.mkdir('./meinvLibs')

    etree = html.etree
    tree = etree.HTML(page_text)
    li_list = tree.xpath("//div[@class='slist']/ul/li")
    for li in li_list:
        img_src = li.xpath('./a/img/@src')[0]
        img_src = "https://pic.netbian.com" + img_src
        img_data = requests.get(url=img_src).content  # 请求到图片的二进制数据
        img_alt = li.xpath('./a/img/@alt')[0] + '.jpg'

        img_name = img_alt.encode('iso-8859-1').decode('gbk') # 通用处理中文乱码的方式

        img_Path = './meinvLibs/' + img_name
        np = open(img_Path, "wb")
        np.write(img_data)
        # print(img_src)
        print(img_name + "...下载完成")