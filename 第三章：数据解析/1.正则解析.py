# -*- coding:utf-8 -*-
"""
Author: Mohan Ren
Date: 07//04//2021//
"""

# 需求：爬取糗事百科中热图板块下所有的热图图片
import re
import requests
import os

if __name__ == "__main__":
    # 创建一个文件夹，保存所有的图片
    if not os.path.exists('./retuLibs'):
        os.mkdir('./retuLibs')


    url = "https://www.qiushibaike.com/imgrank/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 Edg/91.0.864.54"
    }
    # 使用通用爬虫对url对应的一整张页面进行爬取
    page_text = requests.get(url=url, headers=headers).text

    # 聚焦爬虫，将页面中所有的图片解析
    '''
    <div class="thumb" >

    <a href="/article/124494253" target="_blank">
    <img src="//pic.qiushibaike.com/system/pictures/12449/124494253/medium/7PIBWTD6IRZE4NQE.jpg" alt="糗事#124494253" class="illustration" width="100%" height="auto">

    </a>
    </div>
    '''

    # 正则 ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>

    ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
    img_src_list = re.findall(ex, page_text, re.S)

    #持续化存储

    # print(img_src_list)
    for src in img_src_list:
        src = "https:" + src #拼接出一个完整的图片url
        img_data = requests.get(url=src).content # 请求到图片的二进制数据
        img_name = src.split('/')[-1] # 生成图片名称
        img_Path = './retuLibs/' + img_name
        fp = open(img_Path, 'wb')
        fp.write(img_data)
        fp.close()
        print(img_name+'下载成功')