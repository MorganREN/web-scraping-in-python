import scrapy
from bossPro.items import BossproItem

class BossSpider(scrapy.Spider):
    name = 'boss'
    # allowed_domains = ['www.zhipin.com/job_detail/?query=python']
    start_urls = ['http://www.zhipin.com/job_detail/?query=python/']

    # 回调函数接受item
    def parse_detail(self, response):
        item = response.meta['item']
        text = response.xpath('.//*[@id="main"]/div[3]/div/div[2]/div[2]/div[1]/div//text()').extract()
        job_disc = ''.join(text)
        item['text'] = job_disc
        print(job_disc)
        yield  item

    def parse(self, response):
        li_list = response.xpath('/html/body/div[1]/div[3]/div/div[3]/ul/li')
        for li in li_list:
            item = BossproItem
            job_name = li.xpath('//span[@class="job_name"]/a/text()').extract_first()
            item['job_name'] = job_name
            # print(job_name)
            detail_url = "https://www.zhipin.com" + li.xpath('.//span[@class="job_name"]/a/@href').extract_first()
            # 对详情页发请求获取详情页的页面源码数据
            # 手动请求的发送
            # 请求传参：meta={}, 可以将meta字典传递给请求对应的回调函数
            yield scrapy.Request(detail_url, callback=self.parse_detail, meta={'item':item})