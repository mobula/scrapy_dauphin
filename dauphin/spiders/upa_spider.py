# -*- coding: utf-8 -*-
# from scrapy.spiders import XMLFeedSpider
import scrapy

from dauphin.items import RssItem


class UpaSpider(scrapy.Spider):
    name = 'upa'
    allowed_domains = ['upa.qc.ca']
    start_urls = ['http://www.upa.qc.ca/fr/communiques/']
    title = 'Communications UPA'

    def parse(self, response):

        for sel in response.xpath('//article[@class="featured-box__wrapper cf"]'):
            item = RssItem()
            item['title'] = sel.xpath('h1/text()')[0].extract()
            item['pubDate'] = sel.xpath('p[@class="featured-box__meta"]/date/@datetime')[0].extract()
            item['link'] = sel.xpath('p[@class="featured-box__cta"]/a/@href')[0].extract()
            item['description'] = sel.xpath('div[@class="featured-box__content"]/p/text()')[0].extract()
            yield item

        for sel in response.xpath('//article/header'):
            item = RssItem()
            item['title'] = sel.xpath('h2/a/text()')[0].extract()
            item['pubDate'] = sel.xpath('p/time/@datetime')[0].extract()
            item['link'] = sel.xpath('h2/a/@href')[0].extract()
            yield item

