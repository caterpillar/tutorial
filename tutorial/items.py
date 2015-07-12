# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Book(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()
    description = scrapy.Field()
    author = scrapy.Field()


class Book2(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()
    book_type1 = scrapy.Field()
    book_type2 = scrapy.Field()


class CsdnblogcrawlspiderItem(scrapy.Item):
    blog_name = scrapy.Field()
    blog_url = scrapy.Field()

