# -*- coding:utf-8 -*-
import requests
from lxml import html
from chaojiying import Chaojiying_Client
"""
Author: Mohan Ren
Date: 07//19//2021//
"""
# 编码流程：
'''
1. 对验证码的识别，获取验证码图片的文字数据
2. 对POST请求进行发送（处理请求参数）
3. 对响应数据进行持久化存储
'''


# 封装识别验证码的函数
def getCodeText(path, data_type):

    chaojiying = Chaojiying_Client('164689704', 'mohanyuehan123', '919739')  # 用户中心>>软件ID 生成一个替换 96001
    im = open(path, 'rb').read()  # 本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
    # print(chaojiying.PostPic(im, 1902))  # 1902 验证码类型  官方网站>>价格体系 3.4+版 print 后要加()
    return chaojiying.PostPic(im, data_type)['pic_str']


if __name__ == "__main__":
    url = "https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 Edg/91.0.864.54"
    }
    page_text = requests.get(url=url, headers=headers).text

    etree = html.etree
    tree = etree.HTML(page_text)
    img_src = "https://so.gushiwen.cn/" + tree.xpath("/html/body/form[1]/div[4]/div[4]/img/@src")[0]
    code_img_data = requests.get(url=img_src, headers=headers).content
    with open('code.jpg', 'wb') as fp:
        fp.write(code_img_data)

    # 使用超级鹰对验证码图片进行识别
    result = getCodeText("./code.jpg", 1902)
    print(result)

    # POST请求的发送
    login_url = "https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx"
    data = {
        '__VIEWSTATE': 'Y3E6X9PL7dtjJ9zUni3IVjC792bcZYVItF5kMVDjwu/VtJL+GZH8XWicyCzkONmbny8livS0Ct6x6tBm8pcyuu/2XmV4geribjC8vMu6D2xB1MqrmyUTUZ5HJFg=',
        '__VIEWSTATEGENERATOR': 'C93BE1AE',
        'from': 'http://so.gushiwen.cn/user/collect.aspx',
        'email': '15738390010',
        'pwd': '123456789',
        'code': result,
        'denglu': '登录',
    }

    response = requests.post(url=login_url, data=data, headers=headers)

    print(response.status_code) # 验证post请求是否成功，若为200则成功

    # login_page_text = requests.post(url=login_url, data=data, headers=headers).text
    # with open("renren.html", "w", encoding='utf-8') as np:
    #     np.write(login_page_text)
