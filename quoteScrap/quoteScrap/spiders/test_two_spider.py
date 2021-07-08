import scrapy


class TestTwoSpiderSpider(scrapy.Spider):
    name = 'test_two_spider'
    allowed_domains = ['www.testtwo.com']
    start_urls = ['http://www.testtwo.com/']

    def parse(self, response):
        pass
