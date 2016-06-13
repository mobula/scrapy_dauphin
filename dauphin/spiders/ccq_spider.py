import scrapy

from dauphin.items import RssItem

class DmozSpider(scrapy.Spider):
    name = "ccq"
    allowed_domains = ["ccq.org"]
    start_urls = [
        "http://www.ccq.org/fr-CA/nouvelles?profil=GrandPublic"
    ]

    def parse(self, response):
        rootURL = ["http://www.ccq.org"]
        for sel in response.css('.news'):
            item = RssItem()
            item['title'] = sel.xpath('h3/a/text()').extract()
            link = [''.join(rootURL+sel.xpath('h3/a/@href').extract())]
            item['link'] = link
            item['date'] = sel.css('.nouvellesDate').xpath('text()').extract()
            print 'ITEM: ', item
            yield item
