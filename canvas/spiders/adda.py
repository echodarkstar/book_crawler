# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from canvas.items import Book
from canvas.spiders.first import FirstSpider
from difflib import SequenceMatcher

class AddaSpider(CrawlSpider):
    def similar(a, b):
        return SequenceMatcher(None, a, b).ratio()

    name = "adda"
    def __init__(self, category=None, *args, **kwargs):
        super(AddaSpider, self).__init__(*args, **kwargs)
        self.start_urls = ['http://www.bookadda.com/general-search?searchkey={}'.format(category)]

    allowed_domains = ["www.bookadda.com"]
    rules = [
    	Rule(LinkExtractor(allow = ['.*']))
    ] 
    
    def parse(self, response):
        
        b=response.css('div a::text').extract()
        # with open('amazon.txt', 'r') as file:
        #     k = file.read()
        # print(k)

        if b:
            a= response.selector.xpath('//*[@id="search_container"]/div/div[1]/div/div[2]/ul/li[1]/div[2]/div[1]/a[1]/@href').extract()[0]
            print(a)
            next_page = a
            if next_page is not None:
                   next_page = response.urljoin(next_page)
                   yield scrapy.Request(next_page, callback=self.product_parse)

    def product_parse(self, response):
        book = Book()
        book['title'] = response.selector.xpath('//*[@id="prdctdetl"]/div[2]/h1/text()').extract()[0]
        book['author'] = response.selector.xpath('//*[@id="prdctdetl"]/div[2]/span[2]/a/text()').extract()[0]
        book['btype'] = response.selector.xpath('//*[@id="prdctdetl"]/div[2]/span[1]/text()').extract()[0]
        book['price'] = response.selector.xpath('//*[@itemprop="price"]/text()').extract()[0]         
        book['website']= "Bookadda"
        yield book