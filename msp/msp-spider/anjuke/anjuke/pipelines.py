# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import pymysql

class AnjukePipeline(object):

    def __init__(self):
        self.f = open("anjuke.json", "w")
        self.f.write("[\n")
        # 创建连接
        self.conn = pymysql.connect(host='120.27.98.100', port=3306, user='marin', passwd='marin110', db='site_base', charset='utf8')
        # 创建游标
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        content = json.dumps(dict(item), ensure_ascii=False).replace("\\t", "").replace("\\n","") + ", \n"
        self.f.write(content)
        self.cursor.execute("insert into g_house (name,address,room,price,link, source) values ('%s','%s','%s',%d,'%s')" % \
                            (item['name'], item['address'], ','.join(item['rooms']), item['price'], item['link'], "安居客"))
        self.conn.commit()
        return item

    def close_spider(self, spider):
        self.f.write("]")
        self.f.close()
        self.cursor.close()
        self.conn.close()
