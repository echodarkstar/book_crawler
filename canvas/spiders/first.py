# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from canvas.items import Book


class FirstSpider(CrawlSpider):
    name = "first"
    def __init__(self, category=None, *args, **kwargs):
        super(FirstSpider, self).__init__(*args, **kwargs)
        self.start_urls = ['http://www.amazon.in/s/ref=nb_sb_noss?url=search-alias%3Dstripbooks&field-keywords={}'.format(category)]
        

    allowed_domains = ["www.amazon.in"]
    # start_urls = ['http://www.amazon.in/s/ref=nb_sb_noss?url=search-alias%3Dstripbooks&field-keywords=death+note']

    rules = [
    	Rule(LinkExtractor(allow = ['.*']))
    ]
    
    def parse(self, response):
        b=response.selector.xpath('//*[@id="result_0"]/div/div/div/div[2]/div[2]/a/@href').extract()
        if b:
        	a= response.selector.xpath('//*[@id="result_0"]/div/div/div/div[2]/div[2]/a/@href').extract()[0]
        	
        	next_page = a
        	if next_page is not None:
                   next_page = response.urljoin(next_page)
                   yield scrapy.Request(next_page, callback=self.product_parse)

    def product_parse(self, response):
    	book = Book()
    	book['title'] = response.selector.xpath('//*[@id="productTitle"]/text()').extract()[0]
    	if response.selector.xpath('//*[@id="byline"]/span/span[1]/a[1]/text()').extract():
    		book['author'] = response.selector.xpath('//*[@id="byline"]/span/span[1]/a[1]/text()').extract()[0]
    	else:
    		book['author'] = response.selector.xpath('//*[@id="byline"]/span/a/text()').extract()[0]

    	if response.selector.xpath('//*[@id="soldByThirdParty"]/span/text()').extract():
    		book['price'] = response.selector.xpath('//*[@id="soldByThirdParty"]/span/text()').extract()[0]
    	else:
    		book['price'] = response.selector.xpath('//*[@id="unqualifiedBuyBox"]/div/div[1]/span/text()').extract()[0]

    	book['btype'] = response.selector.xpath('//*[@id="title"]/span[2]/text()').extract()[0]
    	book['website']="Amazon"
    	with open("amazon.txt", "w") as file:
    		file.write(book['author'])
    	yield book
