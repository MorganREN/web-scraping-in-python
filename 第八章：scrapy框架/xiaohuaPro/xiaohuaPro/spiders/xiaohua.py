import scrapy


class XiaohuaSpider(scrapy.Spider):
    name = 'xiaohua'
    # allowed_domains = ['http://www.521609.com/meinvxiaohua/']
    start_urls = ['http://www.521609.com/meinvxiaohua//']

    # 生成一个通用的url
    url = 'http://www.521609.com/meinvxiaohua/list12%d.html'
    page_num = 2

    def parse(self, response):
        pic_list = response.xpath('//*[@id="content"]/div[2]/div[2]/ul/li')
        for pic in pic_list:
            # pic_href = 'http://www.521609.com/' + pic.xpath('./a[1]/@href')[1].extract()
            pic_name = pic.xpath('./a[2]/text() | ./a[2]/b/text()').extract_first()
            print(pic_name)

        if self.page_num <= 11:
            new_url = format(self.url%self.page_num)
            self.page_num += 1
            # 手动请求发送:callback回调函数是专门用作于数据解析
            yield scrapy.Request(url=new_url, callback=self.parse)