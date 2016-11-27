# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Book(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    website = scrapy.Field()
    title = scrapy.Field()
    author = scrapy.Field()
    price = scrapy.Field()
    btype = scrapy.Field()
    rating = scrapy.Field()
    blurb = scrapy.Field()