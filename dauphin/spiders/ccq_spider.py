# -*- coding: utf-8 -*-
import scrapy

from dauphin.items import RssItem
from HTMLParser import HTMLParser


class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def handle_charref(self, name):
        self.handle_data(self.unescape('&#{};'.format(name)))
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    html = html.encode('utf8')
    s = MLStripper()
    s.feed(html)
    return unicode(s.get_data(), 'utf-8')


class CcqSpider(scrapy.Spider):
    name = "ccq"
    allowed_domains = ["ccq.org"]
    start_urls = ["http://www.ccq.org/fr-CA/nouvelles?profil=GrandPublic"]
    root_url = "http://www.ccq.org"
    title = "Nouvelles CCQ"
    description = "Mises à jour de la Comission de la Construction du Québec"

    def parse(self, response):

        for sel in response.css('.news'):
            item = RssItem()
            item['title'] = sel.xpath('h3/a/text()')[0].extract()
            link = self.root_url + sel.xpath('h3/a/@href')[0].extract()
            item['link'] = link
            item['guid'] = link
            item['description'] = strip_tags(sel.xpath('div[@class="summary"]')[0].extract())
            # TODO: RFC-822 date-time
            item['pubDate'] = sel.xpath('div[@class="nouvellesDate"]/text()')[0].extract()
            yield item

