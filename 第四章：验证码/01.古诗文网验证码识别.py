# -*- coding:utf-8 -*-
"""
Author: Mohan Ren
Date: 07//18//2021//
"""
import requests
from lxml import html
from chaojiying import Chaojiying_Client

# 封装识别验证码的函数
def getCodeText():
    chaojiying = Chaojiying_Client('164689704', 'mohanyuehan123', '919739')  # 用户中心>>软件ID 生成一个替换 96001
    im = open('code.jpg', 'rb').read()  # 本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
    # print(chaojiying.PostPic(im, 1902))  # 1902 验证码类型  官方网站>>价格体系 3.4+版 print 后要加()
    return chaojiying.PostPic(im, 1902)['pic_str']


if __name__ == "__main__":
    url = "https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 Edg/91.0.864.54"
    }

    page_text = requests.get(url=url, headers=headers).text
    etree = html.etree
    tree = etree.HTML(page_text)
    img_src ="https://so.gushiwen.cn/" + tree.xpath("/html/body/form[1]/div[4]/div[4]/img/@src")[0]
    img_data = requests.get(url=img_src, headers=headers).content
    # 保存验证码图片
    with open("./code.jpg", "wb") as fp:
        fp.write(img_data)

    # 调用超级鹰
    print(getCodeText())