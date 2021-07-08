import scrapy


class TestThreeSpiderSpider(scrapy.Spider):
    name = 'test_three_spider'
    allowed_domains = ['www.testthree.com']
    start_urls = ['http://www.testthree.com/']

    def parse(self, response):
        pass
