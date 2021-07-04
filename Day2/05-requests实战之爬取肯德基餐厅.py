# -*- coding:utf-8 -*-
"""
Author: Mohan Ren
Date: 07//01//2021//
"""
import requests
import json

if __name__ == "__main__":
    url = "http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 Edg/91.0.864.54"
    }

    city = input("What city: ")
    pages = 1 # 页数
    page_number = 0 # 第一次检测页数
    state = True
    while pages != 0:
        page_number += 1
        data = {
            "cname": "",
            "pid": '',
            'keyword': city,
            'pageIndex': '1',
            'pageSize': page_number
        }
        response = requests.post(url=url, data=data, headers=headers)
        text = response.text
        pages -= 1

    file_name = "./"+city+".json"
    fp = open(file_name, 'w', encoding='utf-8')
    json.dump(rest_obj, fp=fp, ensure_ascii=False)

    print("Over")

