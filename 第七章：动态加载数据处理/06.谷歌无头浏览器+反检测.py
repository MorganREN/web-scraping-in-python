# -*- coding:utf-8 -*-
"""
Author: Mohan Ren
Date: 08//15//2021//
"""
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions # 实现规避检测
from time import sleep
from selenium.webdriver.chrome.options import Options # 实现无头界面

if __name__ == "__main__":
    # 无可视化界面（无头浏览器） phantomJs
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')


    # 如何实现让selenium规避被检测到的风险
    options = ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    driver = Chrome(options=options)

    bro = webdriver.Chrome(executable_path='./chromedriver.exe', chrome_options=chrome_options, options=options)
    bro.get('https://www.baidu.com')

    print(bro.page_source)
    sleep(2)
    bro.quit()