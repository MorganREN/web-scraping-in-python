# -*- coding:utf-8 -*-
"""
Author: Mohan Ren
Date: 08//11//2021//
"""
import requests
from lxml import html
from multiprocessing.dummy import Pool
# 需求：爬取梨视频的视频数据
headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 Edg/91.0.864.54"
    }
url = 'https://www.pearvideo.com/category_5'
# 原则：线程池处理的是阻塞且耗时的操作
page_text = requests.get(url=url, headers=headers).text
etree = html.etree
tree = etree.HTML(page_text)
li_list = tree.xpath('/html/body/div[2]/div[1]/div/ul/li')
url_list = []
for li in li_list:
    detail_url = 'https://www.pearvideo.com/' + str(li.xpath('./div/a/@href')[0])
    name = li.xpath('./div/a/div[2]/text()')[0] + '.mp4'
    # url_list.append(detail_url)
    # print(detail_url)
    # print(name)
    # 对详情页的url发起请求
    detail_page_text = requests.get(url=detail_url, headers=headers).text
    # 从详情页中解析出视频的地址url
    # 从这里其遭遇了梨视频的反爬机制，详情解决办法参考https://www.bilibili.com/video/BV1Uo4y1o79n
    video_id = detail_url.split("_")[1]
    video_href = "https://www.pearvideo.com/videoStatus.jsp?contId=" + video_id
    headers_with_id = {
        "Referer": detail_url,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 Edg/91.0.864.54"
    }
    video_url = requests.get(url=video_href, headers=headers_with_id).json()['videoInfo']['videos']['srcUrl']
    # https: // video.pearvideo.com / mp4 / adshort / 20210811 / cont - 1738511 - 15744092 _adpkg - ad_hd.mp4 可以
    # https: // video.pearvideo.com / mp4 / adshort / 20210811 / 1628736278922  - 15744092 _adpkg - ad_hd.mp4 失败
    # 解决办法：通过观察找到不同点，讲内容进行替换成(cont-id)即可
    video_url = video_url.replace(video_url.split('/')[-1].split('-')[0], 'cont-' + video_id)
    # print(video_url) # 反爬成功！！！
    dic = {
        'name': name,
        'url': video_url
    }
    url_list.append(dic)
print(url_list)

def get_video(dic):
    data = requests.get(url=dic['url'], headers=headers).content
    print(dic['name'], 'Downloading......\n')
    # 持久化存储操作
    with open(dic['name'], 'wb') as fp:
        fp.write(data)
        print(dic['name'], 'Done!\n')


# 使用线程池对视频数据进行请求（较为耗时的阻塞操作）
pool = Pool(4)
pool.map(get_video, url_list)
pool.close()
pool.join()
