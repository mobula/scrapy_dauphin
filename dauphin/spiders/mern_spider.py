# -*- coding: utf-8 -*-
# from scrapy.spiders import XMLFeedSpider
import scrapy

from dauphin.items import RssItem


class MernSpider(scrapy.Spider):
    name = 'mern'
    allowed_domains = ['mern.gouv.qc.ca']
    start_urls = ['http://mern.gouv.qc.ca/presse/communiques.jsp']
    iterator = 'iternodes' # you can change this; see the docs
    itertag = 'item' # change it accordingly

    def parse_node(self, response, selector):
        i = DauphinItem()
        #i['url'] = selector.select('url').extract()
        #i['name'] = selector.select('name').extract()
        #i['description'] = selector.select('description').extract()
        return i

