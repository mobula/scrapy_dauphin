# -*- coding: utf-8 -*-
# from scrapy.spiders import XMLFeedSpider
import scrapy

from dauphin.items import RssItem, RssChannel


class UpaSpider(scrapy.Spider):
    name = 'upa'
    allowed_domains = ['upa.qc.ca']
    start_urls = ['http://www.upa.qc.ca/fr/communiques/']

    def parse(self, response):
        filename = response.url.split("/")[-2] + '.html'

        # self.channel = self.parse_channel(response)

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

    def _parse_channel(self, response):

        channel = RssChannel()
        channel['title'] = response.xpath('//title/text()').extract()[0]
        channel['description'] = "L'UPA est passé par là"
        channel['link'] = self.start_urls[0]
        # channel.lastBuildDate = now()

        return channel
