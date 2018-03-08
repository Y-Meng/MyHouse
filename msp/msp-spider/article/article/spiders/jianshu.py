# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from article.items import ArticleItem


class JianshuSpider(scrapy.Spider):
    name = 'jianshu'
    allowed_domains = ['jianshu.com']
    base_url = 'https://www.jianshu.com/trending/weekly?page='
    page = 1
    start_urls = [base_url + str(page)]

    def parse(self, response):
        for li in response.css('.note-list').xpath('li'):
            url = 'https://www.jianshu.com' + li.xpath('div[1]/a[1]/@href').extract()[0]
            yield Request(url, callback=self.parse_article)

        if self.page < 10:
            self.page += 1
            yield Request(self.base_url + str(self.page))

    def parse_article(self, response):
        item = ArticleItem()
        item['url'] = response.url
        yield item
