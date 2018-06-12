# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


import json,codecs,time
import pymongo
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class KeywordspiderPipeline(object):
    def __init__(self):
        self.baidu      = codecs.open('keyword.csv','wb+',encoding='utf-8')
        client          = pymongo.MongoClient('localhost',27017)
        db              = client['keyword']
        collection      = time.strftime('%Y-%m-%d',time.localtime())
        self.collection = db[collection]
        self.collection.remove()

    def process_item(self, item, spider):
        if item["engine"] == '百度风云榜':
            item = dict(item)
            line = json.dumps(item)+'\n'
            self.baidu.write(line.decode('unicode_escape'))
            self.collection.insert(item)
