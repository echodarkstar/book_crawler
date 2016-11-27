# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from canvas.items import Book


class EbaySpider(CrawlSpider):
    name = "ebay"
    def __init__(self, category=None, *args, **kwargs):
        super(EbaySpider, self).__init__(*args, **kwargs)
        self.start_urls = ['http://www.ebay.in/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw={}&_sacat=267'.format(category)]
        

    allowed_domains = ["www.ebay.in"]
    # start_urls = ['http://www.amazon.in/s/ref=nb_sb_noss?url=search-alias%3Dstripbooks&field-keywords=death+note']

    rules = [
    	Rule(LinkExtractor(allow = ['.*']))
    ]
    
    def parse(self, response):
        b=response.selector.xpath('//*[@class="vip"]/@href').extract()
        if b:
        	a= response.selector.xpath('//*[@class="vip"]/@href').extract()[0]
        	# yield {
        	# 	'book' : response.css('a h2::text').extract_first() ,
        	# 	'link' : a
        	# }
        	next_page = a
        	if next_page is not None:
                   next_page = response.urljoin(next_page)
                   yield scrapy.Request(next_page, callback=self.product_parse)

    def product_parse(self, response):
    	book = Book()
    	book['title'] = response.selector.xpath('//*[@id="itemTitle"]/text()').extract()[0]
    	book['author'] = response.selector.xpath('//*[@id="mainContent"]/div/div[5]/div/div/div[4]/div/div/div[8]/div/div/dl/dd[3]/span/text()').extract()
    	book['price'] = response.selector.xpath('//*[@id="prcIsum"]/text()').extract()[0]
    	book['btype'] = response.selector.xpath('//*[@id="vi-desc-maincntr"]/div[4]/div/table/tbody/tr[2]/td[4]/span/text()').extract()
    	book['website']="Amazon"
    	yield book
