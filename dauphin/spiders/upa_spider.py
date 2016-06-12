# -*- coding: utf-8 -*-
# from scrapy.spiders import XMLFeedSpider
import scrapy

from dauphin.items import RssItem


class UpaSpider(scrapy.Spider):
    name = 'upa'
    allowed_domains = ['upa.qc.ca']
    start_urls = ['http://www.upa.qc.ca/fr/communiques/']

    def parse(self, response):
        filename = response.url.split("/")[-2] + '.html'
        page_title = response.xpath('//title/text()').extract()[0]
        print page_title

        for sel in response.xpath('//article'):
            item = RssItem()
            item['title'] = sel.xpath('header/h2/a/text()').extract()
            item['date'] = sel.xpath('header/p/time/@datetime').extract()
            item['link'] = sel.xpath('header/h2/a/@href').extract()
            # desc = sel.xpath('text()').extract()
            yield item
