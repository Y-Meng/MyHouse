# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ArticlePipeline(object):

    def __init__(self):
        self.f = open("articles.json", "w")
        self.f.write("[\n")

    def process_item(self, item, spider):
        self.f.write('"' + item['url'] + '",\n')
        return item

    def close_spider(self, spider):
        self.f.write("]")
        self.f.close()
