# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RssItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    guid = scrapy.Field()
    description = scrapy.Field()
    pubDate = scrapy.Field()
    # author = scrapy.Field()
    # category = scrapy.Field()
