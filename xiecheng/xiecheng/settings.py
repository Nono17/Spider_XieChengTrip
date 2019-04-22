# -*- coding: utf-8 -*-

# Scrapy settings for xiecheng project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'xiecheng'

SPIDER_MODULES = ['xiecheng.spiders']
NEWSPIDER_MODULE = 'xiecheng.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'xiecheng (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 2
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    #   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    #   'Accept-Language': 'en',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
    # 'cookie': 'gad_city=96617ee7af8aedd02bbece8583e0066e; _ga=GA1.2.515639900.1555635158; _gid=GA1.2.2007900916.1555635158; MKT_Pagesource=PC; _RSG=T1aXJZWLVA2iL2DG9IC6S9; _RDG=284ddfe3dd27432a78077ad19549d3eb4b; _RGUID=229f5608-d386-405d-9706-31225034256c; _abtest_userid=3f4f8b76-b67d-4c7b-a569-a0e51186a7b4; ASP.NET_SessionSvc=MTAuMjguMTEyLjIxfDkwOTB8amlucWlhb3xkZWZhdWx0fDE1NTE5NTQ4MDQ4ODU; _RF1=221.220.203.4; _bfa=1.1555635155352.3ir9mz.1.1555656436049.1555671385497.4.117; _bfs=1.25; _gat=1; _jzqco=%7C%7C%7C%7C1555635158169%7C1.1974601113.1555635157792.1555677188958.1555677707675.1555677188958.1555677707675.undefined.0.0.95.95; __zpspc=9.4.1555671387.1555677707.20%234%7C%7C%7C%7C%7C%23; _bfi=p1%3D290660%26p2%3D290660%26v1%3D117%26v2%3D116',
    # 'Referer': 'https://you.ctrip.com/sight/nanjing9/s0-p1.html'
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'xiecheng.middlewares.XiechengSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'xiecheng.middlewares.XiechengDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'xiecheng.pipelines.XiechengPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
