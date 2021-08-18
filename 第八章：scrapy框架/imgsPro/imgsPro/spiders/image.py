import scrapy


class ImageSpider(scrapy.Spider):
    name = 'image'
    # allowed_domains = ['sc.chinaz.com/tupian/']
    start_urls = ['http://sc.chinaz.com/tupian//']

    def parse(self, response):
        div_list = response.xpath('//*[@id="container"]/div')
        for div in div_list:
            img = div.xpath('div[1]/a/img/@src').extract_first()
            print(img)
