# -*- coding:utf-8 -*-
"""
Author: Mohan Ren
Date: 08//15//2021//
"""
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options

if __name__ == "__main__":
    # 无可视化界面（无头浏览器） phantomJs
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')

    bro = webdriver.Chrome(executable_path='./chromedriver.exe', chrome_options=chrome_options)
    bro.get('https://www.baidu.com')

    print(bro.page_source)
    sleep(2)
    bro.quit()