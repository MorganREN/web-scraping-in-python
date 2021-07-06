# -*- coding:utf-8 -*-
"""
Author: Mohan Ren
Date: 07//06//2021//
"""
from lxml import html

if __name__ == "__main__":
    # 实例化一个etree对象
    etree = html.etree
    tree = etree.parse('./test.html', etree.HTMLParser())
    # r = tree.xpath('/html/body/div')
    # r = tree.xpath('/html//div')
    # r = tree.xpath('//div')
    r = tree.xpath('//span[3]/text()')[0]
    print(r)