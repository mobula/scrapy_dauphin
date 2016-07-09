# -*- coding: utf-8 -*-
import time

from scrapy.conf import settings
from scrapy.exporters import XmlItemExporter


class RssItemExporter(XmlItemExporter):

    def __init__(self, *args, **kwargs):
        self.rss_element = 'rss'
        self.channel_element = 'channel'

        self.channel_title = kwargs.pop('channel_title', None)
        self.channel_link = kwargs.pop('channel_link', None)
        self.channel_description = kwargs.pop('channel_description', None)
        self.channel_atom_link = kwargs.pop('channel_atom_link', None)

        self.datetime_format = settings.get('RSS_DATETIME_FORMAT')

        super(RssItemExporter, self).__init__(*args, **kwargs)

    def start_exporting(self):
        self.xg.startDocument()
        self.xg.startElement(self.rss_element, { 'version':'2.0', 'xmlns:atom':'http://www.w3.org/2005/Atom' })
        self.xg.startElement(self.channel_element, {})
        # TODO: export as self-closing tag + add attr.
        # https://validator.w3.org/feed/docs/warning/MissingAtomSelfLink.html
        # self._export_xml_field('atom:link', self.channel_atom_link)
        self._export_xml_field('title', self.channel_title)
        self._export_xml_field('link', self.channel_link)
        self._export_xml_field('description', self.channel_description)
        self._export_xml_field('lastBuildDate', time.strftime(self.datetime_format, time.localtime()))
        self._export_xml_field('pubDate', time.strftime(self.datetime_format, time.localtime()))
        self._export_xml_field('generator', 'scrapy')

    def finish_exporting(self):
        self.xg.endElement(self.channel_element)
        self.xg.endElement(self.rss_element)
        self.xg.endDocument()
