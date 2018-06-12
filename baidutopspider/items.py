# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class KeywordspiderItem(scrapy.Item):
    keyword = scrapy.Field()
    keyword_cates = scrapy.Field()
    keyword_rank = scrapy.Field()
    keyword_day = scrapy.Field()
    keyword_index =scrapy.Field()
    keyword_new_url = scrapy.Field()
    keyword_new_pic = scrapy.Field()
    scrapy_time =scrapy.Field()
    engine =scrapy.Field()
