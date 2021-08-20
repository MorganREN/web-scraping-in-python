import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from sunPro.items import SunproItem
from sunPro.items import DetailItem


# 需求：爬取sun网站中的编号，标题，内容，编号
class SunSpider(CrawlSpider):
    name = 'sun'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://wz.sun0769.com/political/index/politicsNewest?id=1&page=0']

    link = LinkExtractor(allow=r'id=1&page=\d+')  # 链接提取器：根据指定规则(allow='正则')进行指定链接的提取
    link_detail = LinkExtractor(allow=r'id=\d+')
    rules = (
        # 规则解析器：将链接提取器提取到的链接进行指定规则(callback)的解析操作
        # follow的作用:True(可以将链接提取器继续做用到链接提取器提取到的链接做对应的页面中)
        Rule(link, callback='parse_item', follow=True),
        Rule(link_detail, callback='parse_detail')
    )


    # 解析新闻编号和新闻标题
    # 如下两个解析方法中是不可以实现请求传参的
    # 如法将两个解析方法解析的数据存储到同一个item中，可以一次存储到两个item
    def parse_item(self, response):
        li_list = response.xpath('/html/body/div[2]/div[3]/ul[2]/li')
        for li in li_list:
            new_num = li.xpath('./span[1]/text()').extract_first()
            new_title = li.xpath('./span[3]/a/text()').extract_first()
            # print(new_num, new_title)
            item = SunproItem()
            item['title'] = new_title
            item['new_num'] = new_num

            yield item

    def parse_detail(self, response):
        num = response.xpath('/html/body/div[3]/div[2]/div[2]/div[1]/span[4]/text()').extract_first()
        content = response.xpath('/html/body/div[3]/div[2]/div[2]/div[2]/pre/text()').extract_first()
        content = ''.join(content)
        item = DetailItem()
        item['new_content'] = content
        item['new_id'] = num

        yield item