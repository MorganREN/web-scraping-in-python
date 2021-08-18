import scrapy


class ImageSpider(scrapy.Spider):
    name = 'image'
    # allowed_domains = ['sc.chinaz.com/tupian/']
    start_urls = ['http://sc.chinaz.com/tupian//']

    def parse(self, response):
        div_list = response.xpath('//*[@id="container"]/div')
        for div in div_list:
            # 使用src2这一伪属性是由于该站的反扒机制：在未浏览情况下，img的src属性为src2
            src = div.xpath('div[1]/a/img/@src2').extract_first()
            print(src)
