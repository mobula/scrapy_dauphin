# -*- coding: utf-8 -*-

# Override scrapy feed exporter to add rss support
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging

from scrapy.extensions.feedexport import FeedExporter as _FeedExporter
from scrapy.extensions.feedexport import SpiderSlot

logger = logging.getLogger(__name__)


class FeedExporter(_FeedExporter):

    def __init__(self, settings):
        super(FeedExporter, self).__init__(settings)

    def open_spider(self, spider):
        uri = self.urifmt % self._get_uri_params(spider)
        print('uri: ' + uri)
        storage = self._get_storage(uri)
        file = storage.open(spider)
        extra = {
            'channel_title': getattr(spider, 'title', None),
            'channel_link': spider.start_urls[0],
            'channel_description': getattr(spider, 'description', None),
        }
        exporter = self._get_exporter(file, fields_to_export=self.export_fields, extra=extra)
        exporter.start_exporting()
        self.slot = SpiderSlot(file, exporter, storage, uri)

    def close_spider(self, spider):
        return super(FeedExporter, self).close_spider(spider)

    def item_scraped(self, item, spider):
        return super(FeedExporter, self).item_scraped(item, spider)
