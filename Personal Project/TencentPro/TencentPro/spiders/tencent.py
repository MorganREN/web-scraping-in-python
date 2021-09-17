import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from TencentPro.items import TencentproItem


class TencentSpider(CrawlSpider):
    name = 'tencent'
    allowed_domains = ['careers.tencent.com']
    start_urls = ['https://careers.tencent.com/tencentcareer/api/post/Query?categoryId=40001001,40001002,40001003,40001004,40001005,40001006&parentCategoryId=&attrId=&keyword=&pageIndex=1&pageSize=10&language=zh-cn&area=cn']

    def parse_item(self, response):
        json = response.json()
        datas = json.get("Data").get("Posts")
        for data in datas:
            item = TencentproItem()
            item['job_name'] = data.get("RecruitPostName")
            item['address'] = data.get("LocationName")
            item['job_intro'] = data.get("Responsibility").replace('\n', ' ')
            yield item
        # for i in range(2, 4):
        #     next_url = f'https://careers.tencent.com/tencentcareer/api/post/Query？categoryId=40001001,40001002,40001003,40001004,40001005,40001006&pageIndex={i}&pageSize=10&language=zh-cn&area=cn'
        #     yield scrapy.Request(
        #         next_url,
        #         callback=self.parse
        #     )
