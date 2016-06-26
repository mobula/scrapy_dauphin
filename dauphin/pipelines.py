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
        filename = '%s_feed.xml' % spider.name
        file = open(filename, 'w+b')
        self.files[spider] = file
        # TODO: add feed root url to channel_atom_link
        self.exporter = RssItemExporter(
            file,
            channel_title = getattr(spider, 'title', None),
            channel_link = spider.start_urls[0],
            channel_description = getattr(spider, 'description', None),
            channel_atom_link = filename)
        self.exporter.start_exporting()

    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        file = self.files.pop(spider)
        file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
