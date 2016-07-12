# -*- coding: utf-8 -*-
import datetime
import locale

import scrapy

from dauphin.items import RssItem


class UpaSpider(scrapy.Spider):
    name = 'upa'
    allowed_domains = ['upa.qc.ca']
    start_urls = ['http://www.upa.qc.ca/fr/communiques/']
    title = "Communications UPA"
    description = u"Communiqués de l'Union des Producteurs Agrigoles du Québec"
    in_datetime_fmt = '%Y-%m-%dT%H:%M:%S+00:00'
    rss_datetime_fmt = '%a, %d %b %Y %H:%M:%S +0000'

    def parse(self, response):

        for sel in response.xpath('//article[@class="featured-box__wrapper cf"]'):
            item = RssItem()
            item['title'] = sel.xpath('h1/text()')[0].extract()
            item['pubDate'] =  self._to_rss_date(sel.xpath('p[@class="featured-box__meta"]/date/@datetime')[0].extract())
            item['link'] = sel.xpath('p[@class="featured-box__cta"]/a/@href')[0].extract()
            # TODO: guid
            item['description'] = sel.xpath('div[@class="featured-box__content"]/p/text()')[0].extract()
            yield item

        for sel in response.xpath('//article/header'):
            item = RssItem()
            item['title'] = sel.xpath('h2/a/text()')[0].extract()
            item['pubDate'] = self._to_rss_date(sel.xpath('p/time/@datetime')[0].extract())
            item['link'] = sel.xpath('h2/a/@href')[0].extract()
            yield item

    def _to_rss_date(self, datestr):
        loc = locale.getlocale() # store current locale
        d = datetime.datetime.strptime(datestr, self.in_datetime_fmt)
        locale.setlocale(locale.LC_ALL, 'C')
        output = d.strftime(self.rss_datetime_fmt)
        locale.setlocale(locale.LC_ALL, loc)
        return output
