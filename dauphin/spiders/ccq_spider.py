# -*- coding: utf-8 -*-
# from scrapy.spiders import XMLFeedSpider
import scrapy

from dauphin.items import RssItem


class CcqSpider(scrapy.Spider):
    name = 'ccq'
    allowed_domains = ['ccq.org']
    start_urls = ['https://www.ccq.org/fr-CA/Nouvelles']
    # iterator = 'iternodes' # you can change this; see the docs
    # itertag = 'item' # change it accordingly

    # def parse_node(self, response, selector):
    #     i = DauphinItem()
    #     #i['url'] = selector.select('url').extract()
    #     #i['name'] = selector.select('name').extract()
    #     #i['description'] = selector.select('description').extract()
    #     return i

    def parse(self, response):
        # filename = response.url.split("/")[-2] + '.html'
        # page_title = response.xpath('//title/text()').extract()[0]
        # print page_title

        # articleSelector = response.xpath('//article')
        # timeSelector = response.xpath('//article//time/@datetime').extract()
        # titleSelector = response.xpath('//article//h2').extract()
        # linkSelector = response.xpath('//article//h2/a/@href').extract()

        for sel in response.xpath('//article'):
            title = sel.xpath('//h2/a/text()').extract()
            # link = sel.xpath('//h2/a/@href').extract()
            # desc = sel.xpath('text()').extract()
            # date_time = sel.xpath('//time/@datetime')
            print title #,  link, date_time

        # with open(filename, 'wb') as f:
        #     f.write(response.body)
