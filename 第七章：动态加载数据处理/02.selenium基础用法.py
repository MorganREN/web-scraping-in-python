# -*- coding:utf-8 -*-
"""
Author: Mohan Ren
Date: 08//13//2021//
"""
from selenium import webdriver
from lxml import html
from time import sleep

if __name__ == "__main__":
    # 实例化一个浏览器对象（传入浏览器的驱动器）
    bro = webdriver.Chrome(executable_path='./chromedriver.exe')

    # 让浏览器发起一个指定url对应请求
    bro.get(url='http://scxk.nmpa.gov.cn:81/xk/')

    # 获取浏览器页面源码数据
    page_text = bro.page_source

    etree = html.etree
    tree = etree.HTML(page_text)
    li_list = tree.xpath("//ul[@id='gzlist']/li")
    for li in li_list:
        name = li.xpath("./dl/@title")
        print(name)
    sleep(4)
    bro.quit()