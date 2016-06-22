# -*- coding: utf-8 -*-
import datetime
from scrapy.exporters import XmlItemExporter


class RssItemExporter(XmlItemExporter):

    def __init__(self, file, *args, **kwargs):
        self.rss_element = 'rss'
        self.channel_element = 'channel'
        self.channel_title = kwargs.pop('channel_title', None)
        self.channel_link = kwargs.pop('channel_link', None)

        super(RssItemExporter, self).__init__(file, **kwargs)

    def start_exporting(self):
        self.xg.startDocument()
        self.xg.startElement(self.rss_element, {})
        self.xg.startElement(self.channel_element, {})
        self._export_xml_field('title', self.channel_title)
        self._export_xml_field('link', self.channel_link)
        self._export_xml_field('pubDate', datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y"))
        self._export_xml_field('generator', 'scrapy')

    def finish_exporting(self):
        self.xg.endElement(self.channel_element)
        self.xg.endElement(self.rss_element)
        self.xg.endDocument()
