# -*- coding:utf-8 -*-
"""
Author: Mohan Ren
Date: 09//22//2021//
"""
from selenium import webdriver
from selenium.webdriver import ActionChains
from lxml import html
import time

if __name__ == '__main__':
    bro = webdriver.Chrome(executable_path='chromedriver.exe')
    bro.get('https://www.hongxiu.com/category/f1_f1_f1_f1_f1_f1_0_1')
    time.sleep(2)
    page_text = bro.page_source

    etree = html.etree
    tree = etree.HTML(page_text)
    items = tree.xpath("//div[@class='right-book-list']/ul/li")
    print(items)
    for item in items:
        dic = {}

        # The link of the img
        imgLink = 'https:' + item.xpath('./div/a/img/@src')[0]
        dic['Img'] = imgLink

        # The title of the book
        title = item.xpath('./div[2]/h3/a/text()')[0]
        dic['title'] = title

        # The author
        author = item.xpath('./div[2]/h4/a/text()')[0]
        dic['author'] = author

        # The type
        type = item.xpath('./div[2]/p/span[1]/text()')[0]
        dic['types'] = type

        # The status
        status = item.xpath('./div[2]/p/span[2]/text()')[0]
        dic['status'] = status

        # The click number
        click_num = item.xpath('./div[2]/p/span[3]/text()')[0]
        dic['click_num'] = click_num

        # The intro
        intro = item.xpath('./div[2]/p[2]/text()')[0]
        dic['intro'] = intro.replace('\n', '')

        print(dic)

    bro.quit()