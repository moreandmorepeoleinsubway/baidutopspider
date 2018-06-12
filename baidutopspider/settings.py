# -*- coding: utf-8 -*-

BOT_NAME = 'keywordspider'

SPIDER_MODULES = ['keywordspider.spiders']
NEWSPIDER_MODULE = 'keywordspider.spiders'

ROBOTSTXT_OBEY = False

COOKIES_ENABLED = False

DOWNLOADER_MIDDLEWARES = {
    'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware':None,
    'keywordspider.middlewares.KeywordMiddleware':400,
    'scrapy.contrib.downloadermiddleware.redirect.RedirectMiddleware':600,
}

ITEM_PIPELINES = {
   'keywordspider.pipelines.KeywordspiderPipeline': 300,
}

