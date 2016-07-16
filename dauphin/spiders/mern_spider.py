# -*- coding: utf-8 -*-
import datetime
import locale

import scrapy
from scrapy.utils.url import canonicalize_url

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
    exclude_sectors = [ 112 ] # Le Ministère = ne respecte pas le filtrage

    def parse(self, response):
        # return self.parse_secteurs(response)
        return self.parse_communiques(response)

    def parse_secteurs(self, response):
        """Récupère les différents secteurs et va chercher les pages dédiées.

        Il y a un problème avec la sous-page "Le ministère", qui retourne toutes les catégories
        """
        selectors = response.xpath('//select[@id="idSecteur"]/option')
        # secteurs = { sel.xpath('@value')[0].extract(): sel.xpath('text()')[0].extract() for sel in selectors }
        for sel in selectors:
            secteur_id = sel.xpath('@value')[0].extract()
            if int(secteur_id) not in self.exclude_sectors:
                secteur = sel.xpath('text()')[0].extract()
                url = response.url + '?idSecteur=' + secteur_id
                yield scrapy.Request(url=url, callback=self.parse_communiques, meta={ 'category': secteur })

    def parse_communiques(self, response):
        category = response.meta.get('category', None)

        communiques = response.css('p.communiques')
        for communique in communiques:
            item = RssItem()
            if category:
                item['category'] = category
            item['pubDate'] = self._to_rss_date(communique.xpath('b/text()').re_first('(.*)\s.*'))
            item['title'] = communique.xpath('a/text()')[0].extract()
            link = self._get_uri(communique.xpath('a//@href')[0].extract())
            item['link'] = link
            item['guid'] = canonicalize_url(link)
            yield scrapy.Request(link, callback=self.parse_detail, meta={ 'item': item })

    def parse_by_category(self, response):
        """ Tentative de trouver les communiqués reliés à une catégorie particulière """
        for cat in response.xpath('//p[@class="ss-titre"]'):
            category = cat.xpath('text()')[0].extract()
            communiques = cat.xpath('following-sibling::*').css('p.communiques')
            for communique in communiques:
                item = RssItem()
                item['category'] = category
                item['pubDate'] = self._to_rss_date(communique.xpath('b/text()').re_first('(.*)\s.*'))
                item['title'] = communique.xpath('a/text()')[0].extract()
                link = self._get_uri(communique.xpath('a//@href')[0].extract())
                item['link'] = link
                item['guid'] = canonicalize_url(link)
                yield scrapy.Request(url=link, callback=self.parse_detail, meta={ 'item': item })

    def parse_detail(self, response):
        item = response.meta.get('item', None)
        contenu = response.xpath('string(//p[@class="contenu"])')[0].extract()
        item['description'] = contenu[:2000] + "..."
        return item

    def _get_uri(self, url):
        return self.root_url + url

    def _to_rss_date(self, datestr):
        loc = locale.getlocale() # store current locale
        locale.setlocale(locale.LC_TIME, 'fr_FR.UTF-8')
        d = datetime.datetime.strptime(datestr.encode('utf-8'), '%d %B %Y')
        locale.setlocale(locale.LC_TIME, 'C')
        output = d.strftime(self.rss_datetime_fmt)
        locale.setlocale(locale.LC_TIME, loc)
        return output
