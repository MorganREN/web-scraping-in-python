# -*- coding:utf-8 -*-
"""
Author: Mohan Ren
Date: 08//15//2021//
"""
from chaojiying import Chaojiying_Client
from selenium import webdriver
from selenium.webdriver import ActionChains
import time

# 封装识别验证码的函数
def getCodeText(path, type):
    chaojiying = Chaojiying_Client('164689704', 'mohanyuehan123', '919739')  # 用户中心>>软件ID 生成一个替换 96001
    im = open(path, 'rb').read()  # 本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
    # print(chaojiying.PostPic(im, 1902))  # 1902 验证码类型  官方网站>>价格体系 3.4+版 print 后要加()
    return chaojiying.PostPic(im, type)['pic_str']

if __name__ == "__main__":
    # 打开12306网页
    bro = webdriver.Chrome(executable_path='chromedriver.exe')
    bro.get('https://kyfw.12306.cn/otn/resources/login.html')
    time.sleep(0.5)

    # 定位账号密码登录
    switch = bro.find_element_by_class_name('login-hd-account')
    switch.click()
    time.sleep(1.5)

    # 保存验证码图片并进行分析，得到坐标
    img = bro.find_element_by_id('J-loginImg')
    detail_img = img.screenshot_as_png
    with open("./img_code.png", 'wb') as np:
        np.write(detail_img)
    coord = getCodeText('./img_code.png', 9004)
    coord_list = coord.split('|') # 将坐标按照|分成列表
    i = 0
    for detail_coord in coord_list:
        good_coord = detail_coord.split(',')
        coord_list[i] = good_coord
        i += 1
    print(coord_list)

    # 定位账号和密码标签和登录标签
    user_input = bro.find_element_by_id('J-userName')
    pwd_input = bro.find_element_by_id('J-password')
    login_btn = bro.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div[5]/a')


    # 输入账号和密码
    time.sleep(1)
    user_input.send_keys('15738390010')
    time.sleep(1)
    pwd_input.send_keys('Ren010218')

    # 点击验证图片
    # 问题：若出现两张以上符合目标，selenium点击一次后再点击另一张时，前一张的标签会消失
    # 解决：将perform()单独拉出到循环外，等所有图片都被点击后再执行动作链；
    # 不然会发生动作链中的动作重复
    action = ActionChains(bro)
    for pic_num in coord_list:
        x = int(pic_num[0])
        y = int(pic_num[1])
        action.move_to_element_with_offset(img, x, y).click()
    action.perform()


    # 点击立即登录
    login_btn.click()
    time.sleep(3) # 此刻休息3秒，使网页加载出滑块，否则会定位失败

    # 防止12306禁止selenium
    script = 'Object.defineProperty(navigator,"webdriver",{get:()=>undefined,});'
    bro.execute_script(script)

    # 定位并点击滑块标签
    # 重新实例化一个新的ActionChain，避免了之前链的影响
    action2 = ActionChains(bro)
    span = bro.find_element_by_xpath('//*[@id="nc_1_n1z"]')
    action2.click_and_hold(span)

    # 滑动滑块并释放动作
    # 问题：尚未解决滑块问题
    action2.move_by_offset(350, 0).perform()
    time.sleep(1)
    action2.release(span)

    time.sleep(10)
    bro.quit()