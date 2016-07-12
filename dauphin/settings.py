# -*- coding: utf-8 -*-

# Scrapy settings for dauphin project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'dauphin'

SPIDER_MODULES = ['dauphin.spiders']
NEWSPIDER_MODULE = 'dauphin.spiders'

# Logging
# LOG_ENABLED = True
# LOG_FILE = 'rss.log'
# LOG_LEVEL = 'ERROR'
# LOG_STDOUT = True


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'dauphin (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

RSS_DATETIME_FORMAT = '%a, %d %b %Y %H:%M:%S %z'
ATOM_DATETIME_FORMAT = '%Y-%m-%dT%H:%M:%SZ'
FEED_DATETIME_FORMAT = RSS_DATETIME_FORMAT


# S3 credentials (dauphin)
# AWS_ACCESS_KEY_ID = # os.environ...
# AWS_SECRET_ACCESS_KEY = # os.environ
AWS_USERNAME = 'dauphin'
AWS_S3_BUCKET = 'dauphin-rss'

# FEED_URI = 'file:///Volumes/Data/Development/code/python/scrapy/dauphin/feeds/%(name)s.rss'
FEED_URI = 's3://dauphin-rss/feeds/%(name)s.rss'
FEED_FORMAT = 'rss'
# FEED_PUBLIC_URI = 'dauphin-rss.s3-website-us-east-1.amazonaws.com/feed/%(name)s.rss'


FEED_EXPORTERS = {
    'rss': 'dauphin.exporters.RssItemExporter',
    # 'atom': 'dauphin.exporters.AtomItemExporter',
}

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 2
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'fr',
}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'dauphin.middlewares.MyCustomSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'dauphin.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
EXTENSIONS = {
    'scrapy.extensions.feedexport.FeedExporter': None,
    'dauphin.feedexport.FeedExporter': 0,
    # 'scrapy_dotpersistence.DotScrapyPersistence': 0,
}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
# }

# DOTSCRAPY_ENABLED = True
# ADDONS_AWS_ACCESS_KEY_ID = AWS_ACCESS_KEY_ID
# ADDONS_AWS_SECRET_ACCESS_KEY = AWS_SECRET_ACCESS_KEY
# ADDONS_AWS_USERNAME = AWS_USERNAME
# ADDONS_S3_BUCKET = AWS_S3_BUCKET


# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
