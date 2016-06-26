# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy import signals

from .exporters import RssItemExporter


class RssExportPipeline(object):

    def __init__(self):
        self.files = {}

    @classmethod
    def from_crawler(cls, crawler):
         pipeline = cls()
         crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
         crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
         return pipeline

    def spider_opened(self, spider):
        file = open('%s_feed.xml' % spider.name, 'w+b')
        self.files[spider] = file
        # TODO: add feed root url to channel_atom_link
        self.exporter = RssItemExporter(file, channel_title=spider.title, \
        channel_link=spider.start_urls[0], channel_description=spider.description, \
        channel_atom_link=spider.name+'_feed.xml')
        self.exporter.start_exporting()

    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        file = self.files.pop(spider)
        file.close()

    def process_item(self, item, spider):
        print('PROCESSING ITEM')
        self.exporter.export_item(item)
        return item
