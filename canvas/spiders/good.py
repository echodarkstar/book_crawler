# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from canvas.items import Book

class GoodSpider(CrawlSpider):
    name = "good"
    def __init__(self, category=None, *args, **kwargs):
        super(GoodSpider, self).__init__(*args, **kwargs)
        self.start_urls = ['https://www.goodreads.com/search?utf8=%E2%9C%93&query={}'.format(category)]

    allowed_domains = ["www.goodreads.com"]
    rules = [
    	Rule(LinkExtractor(allow = ['.*']))
    ] 
    
    def parse(self, response):
        b=response.selector.xpath('//*[@class="bookTitle"]/@href').extract()
        if b:
            a= response.selector.xpath('//*[@class="bookTitle"]/@href').extract()[0]
            next_page = a
            if next_page is not None:
                   next_page = response.urljoin(next_page)
                   yield scrapy.Request(next_page, callback=self.product_parse)

    def product_parse(self, response):
        book = Book()
        # book['title'] = (response.selector.xpath('//*[@id="bookTitle"]/text()').extract()[0]).strip()
        # book['author'] = response.selector.xpath('//*[@itemprop="name"]/text()').extract()[1]
        # book['btype'] = response.selector.xpath('//*[@itemprop="bookFormatType"]/text()').extract()[0]
        book['website']= "Goodreads"
        book['rating'] = response.selector.xpath('//*[@itemprop="ratingValue"]/text()').extract()[0]
        book['count'] = response.selector.xpath('//*[@itemprop="ratingCount"]/text()').extract()[0]
        # book['blurb'] =  ''.join(response.selector.xpath('//*[@id="description"]//span[contains(@style,"none")]/text()').extract()).replace('\xa0','')
        yield book