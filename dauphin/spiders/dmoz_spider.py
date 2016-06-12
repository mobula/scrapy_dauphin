# -*- coding: utf-8 -*-
# from scrapy.spiders import XMLFeedSpider
import scrapy

from dauphin.items import RssItem


class DmozSpider(scrapy.Spider):
    name = 'dmoz'
    allowed_domains = ['dmoz.org']
    start_urls = ['http://www.dmoz.org/Computers/Programming/Languages/Python/Books/']

    def parse(self, response):
        for sel in response.css('.site-item'):
            item = RssItem()
            # item['title'] = u'1'
            item['title'] = sel.css('.title-and-desc').css('.site-title').xpath('text()').extract()
            item['link'] = sel.css('.title-and-desc').xpath('a/@href').extract()
            # item['desc'] = sel.xpath('text()').extract()
            # print title, link #, link, desc
            yield item
