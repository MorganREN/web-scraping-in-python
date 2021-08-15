# -*- coding:utf-8 -*-
"""
Author: Mohan Ren
Date: 08//14//2021//
"""
from selenium import webdriver
from time import sleep

if __name__ == "__main__":
    bro = webdriver.Chrome(executable_path='./chromedriver.exe')
    bro.get('https://qzone.qq.com/')
    bro.switch_to.frame('login_frame')
    switch = bro.find_element_by_id('switcher_plogin')
    switch.click()

    user_name_tag = bro.find_element_by_id('u')
    user_pwd_tag = bro.find_element_by_id('p')

    user_name_tag.send_keys('164689704')
    sleep(1.5)
    user_pwd_tag.send_keys('momomoyueyueyue1')
    sleep(1)

    enter_btn = bro.find_element_by_id('login_button')
    enter_btn.click()

    sleep(3)
    bro.quit()