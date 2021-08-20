import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class SunSpider(CrawlSpider):
    name = 'sun'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://wz.sun0769.com/political/index/politicsNewest?id=1&page=0']

    link = LinkExtractor(allow=r'id=1&page=\d+')  # 链接提取器：根据指定规则(allow='正则')进行指定链接的提取
    rules = (
        # 规则解析器：将链接提取器提取到的链接进行指定规则(callback)的解析操作
        # follow的作用:True(可以将链接提取器继续做用到链接提取器提取到的链接做对应的页面中)
        Rule(link, callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        print(response)
