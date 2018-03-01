import scrapy

from anjuke.items import AnjukeItem


class AjkLoupanSpider(scrapy.Spider):
    name = "anjuke"
    allowed_domains = ["anjuke.com"]
    start_urls = [
        "https://zz.fang.anjuke.com/loupan/all/",
        "https://zz.fang.anjuke.com/loupan/all/p2/",
        "https://zz.fang.anjuke.com/loupan/all/p3/",
        "https://zz.fang.anjuke.com/loupan/all/p4/",
        "https://zz.fang.anjuke.com/loupan/all/p5/",
        "https://zz.fang.anjuke.com/loupan/all/p6/",
        "https://zz.fang.anjuke.com/loupan/all/p7/",
        "https://zz.fang.anjuke.com/loupan/all/p8/",
        "https://zz.fang.anjuke.com/loupan/all/p9/",
        "https://zz.fang.anjuke.com/loupan/all/p10/"
    ]

    def parse(self, response):
        for sel in response.xpath('/html/body/div[2]/div[2]/div[1]/div[3]/div'):
            item = AnjukeItem()
            item['link'] = sel.xpath('@data-link').extract()[0]
            item['name'] = sel.xpath('div/a/h3/span/text()').extract()[0]
            item['address'] = sel.xpath('div/a[2]/span/text()').extract()[0]
            item['rooms'] = sel.xpath('div/a[3]/span/text()').extract()
            price = sel.xpath('a[2]/p/span/text()').extract()[0]
            try:
                item['price'] = int(price)
            except:
                item['price'] = 99999

            yield item



