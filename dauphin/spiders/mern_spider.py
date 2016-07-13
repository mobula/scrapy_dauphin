# -*- coding: utf-8 -*-
import datetime
import locale

import scrapy
from scrapy.linkextractors import LinkExtractor

from dauphin.items import RssItem


class MernSpider(scrapy.Spider):
    name = 'mern'
    allowed_domains = ['mern.gouv.qc.ca']
    start_urls = ['http://mern.gouv.qc.ca/presse/communiques.jsp']
    root_url = "http://mern.gouv.qc.ca/presse/"
    title = "Communiqués MERN"
    description = u"Communiqués du MERN"
    in_datetime_fmt = '%Y-%m-%dT%H:%M:%S+00:00'
    rss_datetime_fmt = '%a, %d %b %Y %H:%M:%S +0000'

    def parse(self, response):
        for cat in response.xpath('//p[@class="ss-titre"]'):
            category = cat.xpath('text()')[0].extract()
            communiques = cat.xpath('following-sibling::*').css('p.communiques')
            for communique in communiques:
                item = RssItem()
                item['category'] = category
                item['pubDate'] = self._to_rss_date(communique.xpath('b/text()').re_first('(.*)\s.*'))
                item['title'] = communique.xpath('a/text()')[0].extract()
                item['link'] = self._get_uri(communique.xpath('a//@href')[0].extract())
                # content_page = self._link_content(link)
                # item['description'] = content_page.css('span.contenu')[0].extract()
                yield item

    def _get_uri(self, url):
        return self.root_url + url

    def _link_content(self, link):
        pass

    def _to_rss_date(self, datestr):
        loc = locale.getlocale() # store current locale
        locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8')
        d = datetime.datetime.strptime(datestr, '%d %B %Y')
        locale.setlocale(locale.LC_ALL, 'C')
        output = d.strftime(self.rss_datetime_fmt)
        locale.setlocale(locale.LC_ALL, loc)
        return output

    # def parse_node(self, response, selector):
    #     i = DauphinItem()
    #     #i['url'] = selector.select('url').extract()
    #     #i['name'] = selector.select('name').extract()
    #     #i['description'] = selector.select('description').extract()
    #     return i
