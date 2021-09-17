# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentproItem(scrapy.Item):
    # define the fields for your item here like:
    job_name = scrapy.Field()  # 岗位名称
    address = scrapy.Field()  # 岗位地址
    job_intro = scrapy.Field()  # 岗位介绍
    pass
