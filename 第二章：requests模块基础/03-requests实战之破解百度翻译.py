# -*- coding:utf-8 -*-
"""
Author: Mohan Ren
Date: 06//30//2021//
"""
import json

import requests

if __name__ == "__main__":
    # 1.指定URL
    post_url = "https://fanyi.baidu.com/sug"
    # 2.进行UA伪装
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 Edg/91.0.864.54"
    }
    # 3.POST请求参数处理，与get方法一致
    word = input("Please input a word: \n")
    data = {
        "kw": word
    }
    # 4.请求发送
    response = requests.post(url=post_url, data=data, headers=headers)
    # 5.获取响应数据: json()方法返回的是obj(如果确认响应数据是json类型的，才可以使用json() )
    dic_obj = response.json()
    # print(dic_obj)

    # 6.持久化输出
    file_name = "./" + word + ".json"
    fp = open(file_name, 'w', encoding="utf-8")
    json.dump(dic_obj, fp=fp, ensure_ascii=False)

    print("Over")
