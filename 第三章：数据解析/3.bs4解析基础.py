# -*- coding:utf-8 -*-
"""
Author: Mohan Ren
Date: 07//05//2021//
"""
from bs4 import BeautifulSoup

if __name__ == "__main__":
    # 将本地的html文档中的数据加载到该对象中
    fp = open('./test.html', 'r', encoding='utf-8')
    soup = BeautifulSoup(fp, 'lxml') # 参数二固定为lxml
    # print(soup.div) #soup.tagName 返回的是html中 第一次 出现的tagName标签

    #find('tagName'):等同于soup.div
    # print(soup.find('div')) #等于soup.div
    #print(soup.find('div', class_ ="hzbscin")) # 注意class_必须有下划线，也可以是id/attr

    # print(soup.find_all('a'))

    # print(soup.select(".hzbbtm")) # 返回的是一个列表，参数内应放置某种选择器（id/class/tag...)

    print(soup.html['xmlns'])



