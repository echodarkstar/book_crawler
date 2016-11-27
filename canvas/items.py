# -*- coding: utf-8 -*-

import scrapy

class Book(scrapy.Item):
    website = scrapy.Field()
    title = scrapy.Field()
    author = scrapy.Field()
    price = scrapy.Field()
    btype = scrapy.Field()
    rating = scrapy.Field()
    blurb = scrapy.Field()
    count = scrapy.Field()