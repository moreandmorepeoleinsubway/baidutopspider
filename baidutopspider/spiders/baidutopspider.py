# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from scrapy.http import FormRequest
from keywordspider.items import KeywordspiderItem
import time,json,sys,re,Queue

class BaidutopspiderSpider(scrapy.Spider):
    name = "baidutop"
    allowed_domains = ["top.baidu.com"]
    start_urls = [
    'http://top.baidu.com/buzz?b=1&c=513',
    'http://top.baidu.com/buzz?b=341&c=513',
    'http://top.baidu.com/buzz?b=42&c=513',
    'http://top.baidu.com/buzz?b=342&c=513',
    'http://top.baidu.com/buzz?b=344&c=513']
    def parse(self,response):
        search_body = response.xpath('//*[@id="main"]/div[2]/div/table/tr')
        try:
            for i in search_body:
                items =  KeywordspiderItem()
                url = response.url
                if   url == 'http://top.baidu.com/buzz?b=1&c=513':
                    items['keyword_cates'] ='实时热点'
                elif url == 'http://top.baidu.com/buzz?b=341&c=513':
                    items['keyword_cates'] ='今日热点'
                elif url == 'http://top.baidu.com/buzz?b=42&c=513':
                    items['keyword_cates'] ='七日热点'
                elif url == 'http://top.baidu.com/buzz?b=342&c=513':
                    items['keyword_cates'] ='民生热点'
                elif url == 'http://top.baidu.com/buzz?b=344&c=513':
                    items['keyword_cates'] ='娱乐热点'
                items['scrapy_time'] = time.strftime('%m-%d-%H',time.localtime())
                items['keyword_day'] = time.strftime('%Y-%m-%d',time.localtime())
                items['engine'] =  '百度风云榜'
                if not i.xpath('.//td[@class="first"]/span/text()').extract_first():
                    print "empty page" 
                else:
                    items['keyword_rank']=i.xpath('.//td[@class="first"]/span/text()').extract_first() 
                    items['keyword']=i.xpath('.//td[@class="keyword"]/a/text()').extract_first()
                    items['keyword_index']=i.xpath('.//td[@class="last"]/span/text()').extract_first()
                    items['keyword_new_url']=i.xpath('.//td[@class="tc"]/a[1]/@href').extract_first()
                    items['keyword_new_pic']=i.xpath('.//td[@class="tc"]/a[3]/@href').extract_first()
                    print "astract over"
                    yield items 

        except Exception as e:
            print  "采集规则有误",e,
