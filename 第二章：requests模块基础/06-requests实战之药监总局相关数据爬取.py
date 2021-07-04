# -*- coding:utf-8 -*-
"""
Author: Mohan Ren
Date: 07//01//2021//
"""
import requests
import json

if __name__ == "__main__":
    # 批量获取不同企业的ID值
    url = "http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 Edg/91.0.864.54"
    }
    # 参数的封装
    id_list = []  # 存储企业的ID
    for page in range(1, 6):
        data = {
            'on': 'true',
            'page': page,
            'pageSize': '15',
            'productName': '',
            'conditionType': '1',
            'applyname': '',
            'applysn': ''
        }

        response = requests.post(url=url, headers=headers, data=data)
        json_ids = response.json()
        for dic in json_ids['list']:
            id_list.append(dic['ID'])

    # print(id_list)
    # 获取企业详情数据
    fp = open('./化妆.json', 'a', encoding='utf-8')
    post_url = "http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById"
    for i in id_list:
        id_data = {
            'id' : i
        }
        spe_json = requests.post(url=post_url, headers=headers, data=id_data).json()
        json.dump(spe_json, fp=fp, ensure_ascii=False)
        fp.write("\n")
    fp.close()
    print("Over")
