from scrapy.exporters import XmlItemExporter


class RssItemExporter(XmlItemExporter):

    def __init__(self, file, **kwargs):
    	super(RssItemExporter, self).__init__(file, **kwargs)

        self.rss_element = 'rss'
        self.channel_element = 'channel'
        # self.channel_title = 'prout'
        # self._configure(kwargs)
        # self.xg = XMLGenerator(file, encoding=self.encoding)

    def start_exporting(self):
        self.xg.startDocument()
        # self.xg.startElement('rss', {})
        self.xg.startElement(self.rss_element, {})
        self.xg.startElement(self.channel_element, {})
        # self.xg.startElement(self.channel_title, {})
        # self.xg.endElement(self.channel_title)
        # self.xg.startElement(self.root_element, {})

    def finish_exporting(self):
        # self.xg.endElement(self.root_element)
        self.xg.endElement(self.channel_element)
        self.xg.endElement(self.rss_element)
        self.xg.endDocument()
