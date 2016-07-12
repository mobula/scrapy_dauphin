# -*- coding: utf-8 -*-
import datetime
import locale
import scrapy

from HTMLParser import HTMLParser

from dauphin.items import RssItem


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
    description = "Mises à jour de la Commission de la Construction du Québec"
    rss_datetime_format = '%a, %d %b %Y %H:%M:%S EST'

    def parse(self, response):

        for sel in response.css('.news'):
            item = RssItem()
            item['title'] = sel.xpath('h3/a/text()')[0].extract()
            link = self.root_url + sel.xpath('h3/a/@href')[0].extract()
            item['link'] = link
            item['guid'] = link
            item['description'] = strip_tags(sel.xpath('div[@class="summary"]')[0].extract())
            item['pubDate'] = self._to_rss_date(sel.xpath('div[@class="nouvellesDate"]/text()')[0].extract())
            yield item

    def _to_rss_date(self, datestr):
        loc = locale.getlocale() # store current locale
        locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8')
        d = datetime.datetime.strptime(datestr, '%d %B %Y')
        locale.setlocale(locale.LC_ALL, 'C')
        output = d.strftime(self.rss_datetime_format)
        locale.setlocale(locale.LC_ALL, loc)
        return output

