# -*- coding: utf-8 -*-
import scrapy

from dauphin.items import RssItem


class CcqSpider(scrapy.Spider):
    name = "ccq"
    allowed_domains = ["ccq.org"]
    start_urls = [
        "http://www.ccq.org/fr-CA/nouvelles?profil=GrandPublic"
    ]
    root_url = ["http://www.ccq.org"]

    def parse(self, response):
        for sel in response.css('.news'):
            item = RssItem()
            item['title'] = sel.xpath('h3/a/text()').extract()
            link = [''.join(self.rootURL+sel.xpath('h3/a/@href').extract())]
            item['link'] = link
            item['date'] = sel.css('.nouvellesDate').xpath('text()').extract()
            yield item

