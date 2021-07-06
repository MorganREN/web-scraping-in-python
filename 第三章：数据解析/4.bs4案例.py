# -*- coding:utf-8 -*-
"""
Author: Mohan Ren
Date: 07//05//2021//
"""

# 爬取三国演义小说所有的章节标题和章节内容
import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    url = "https://www.shicimingju.com/book/sanguoyanyi.html"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 Edg/91.0.864.54"
    }

    sanguo = requests.get(url=url, headers=headers).text
    soup = BeautifulSoup(sanguo, 'lxml') # 实例化BeautifulSoup对象

    sanguo_headers = soup.select('.book-mulu > ul > li')
    fp = open('./sanguoyanyi.txt', 'w', encoding='utf-8')
    for li in sanguo_headers:
        title = li.a.string
        href = "https://www.shicimingju.com" + li.a['href']
        # print(title + "\n")
        # print(href + "\n")
        detail_page_text = requests.get(url=href, headers=headers).text
        #解析出详情页中相关的章节内容
        detail_soup = BeautifulSoup(detail_page_text, 'lxml')
        div_tag = detail_soup.find('div', class_='chapter_content')
        #解析到了章节内容
        content = div_tag.text
        fp.write(title+": \n" + content + "\n")
