import scrapy


class QiubaiSpider(scrapy.Spider):
    name = 'qiubai'
    # allowed_domains = ['https://www.qiushibaike.com/']
    start_urls = ['https://www.qiushibaike.com/text/']

    def parse(self, response):
        # 解析：作者的名称+段子的内容
        div_list = response.xpath('/html/body/div[1]/div/div[2]/div')
        for div in div_list:
            # xpath返回的是列表，但是列表元素一定是selector类型的对象
            # extract可以讲selector中data参数存储的字符串提取出来
            author = div.xpath('./div[1]/a[2]/h2/text()')[0].extract_first()

            # 列表调用了extract之后，则表示将列表中每一个selector对象中data对应的字符串提取了出来
            contents = div.xpath('./a[1]/div[1]/span[1]//text()').extract() #span标签中有其他标签，因此是//text()

            txt = ''
            for content in contents:
                txt = txt + content
            print(author, txt)
            # break


