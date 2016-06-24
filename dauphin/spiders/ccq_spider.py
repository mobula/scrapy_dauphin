# -*- coding: utf-8 -*-
import scrapy

from dauphin.items import RssItem


class CcqSpider(scrapy.Spider):
    name = "ccq"
    allowed_domains = ["ccq.org"]
    start_urls = [
        "http://www.ccq.org/fr-CA/nouvelles?profil=GrandPublic"
    ]
    root_url = "http://www.ccq.org"
    title = "Nouvelles CCQ"

    def parse(self, response):
    
        for sel in response.css('.news'):
            item = RssItem()
            item['title'] = sel.xpath('h3/a/text()')[0].extract()
            link = self.root_url+sel.xpath('h3/a/@href')[0].extract()
            item['link'] = link
            item['pubDate'] = sel.xpath('div[@class="nouvellesDate"]/text()')[0].extract()
            yield item

