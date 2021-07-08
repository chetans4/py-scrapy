import scrapy


class TestspiderSpider(scrapy.Spider):
    name = 'testspider'
    allowed_domains = ['www.test.com']
    start_urls = ['http://www.test.com/']

    def parse(self, response):
        pass
