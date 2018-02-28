# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json


class FangtxPipeline(object):

    def __init__(self):
        self.f = open("fangtianxia.json", "w")
        self.f.write("[\n")

    def process_item(self, item, spider):
        content = json.dumps(dict(item), ensure_ascii=False).replace("\\t", "").replace("\\n","") + ", \n"
        self.f.write(content)
        return item

    def close_spider(self, spider):
        self.f.write("]")
        self.f.close()
