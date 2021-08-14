# -*- coding:utf-8 -*-
"""
Author: Mohan Ren
Date: 08//14//2021//
"""
from selenium import webdriver
import time
if __name__ == "__main__":
    bro = webdriver.Chrome(executable_path='./chromedriver.exe')
    bro.get('https://www.taobao.com/')

    # 定位标签
    search_input = bro.find_element_by_id('q')
    search_key = bro.find_element_by_class_name('btn-search')
    # 进行标签交互
    search_input.send_keys('iphone12') # 搜索框中输入iphone12
    time.sleep(3)

    # 执行一组JS程序
    bro.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(3)

    search_key.click() # 点击搜索按钮

    bro.get('https://www.baidu.com')
    time.sleep(1)
    # 回退
    bro.back()
    time.sleep(1)
    # 前进
    bro.forward()

    time.sleep(3)
    bro.quit()

