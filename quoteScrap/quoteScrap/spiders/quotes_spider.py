import scrapy

class QuoteSpider(scrapy.Spider):
	name = "quotespider"
	start_urls = ['https://quotes.toscrape.com/']

	def parse(self, response):
		title = response.css('title::text').extract()
		yield {'titletext':title}