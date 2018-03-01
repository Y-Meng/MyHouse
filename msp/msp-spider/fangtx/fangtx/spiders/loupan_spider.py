import scrapy

from fangtx.items import FangtxItem


class FangSpider(scrapy.Spider):
    name = "fangtx"
    allowed_domains = ["fang.com"]
    start_urls = [
        "http://newhouse.zz.fang.com/house/s/b91/",
        "http://newhouse.zz.fang.com/house/s/b92/",
        "http://newhouse.zz.fang.com/house/s/b93/",
        "http://newhouse.zz.fang.com/house/s/b94/",
        "http://newhouse.zz.fang.com/house/s/b95/",
        "http://newhouse.zz.fang.com/house/s/b96/",
        "http://newhouse.zz.fang.com/house/s/b97/",
        "http://newhouse.zz.fang.com/house/s/b98/",
        "http://newhouse.zz.fang.com/house/s/b99/",
        "http://newhouse.zz.fang.com/house/s/b910/"
    ]
    
    def parse(self, response):
        for sel in response.selector.xpath("/html/body/div[9]/div/div[1]/div[1]/div/div/ul/li"):
            item = FangtxItem()
            item['link'] = sel.xpath('div/div[2]/div[1]/div[1]/a/@href').extract()[0]
            item['name'] = sel.xpath('div/div[2]/div[1]/div[1]/a/text()').extract()[0]
            item['rooms'] = sel.css('.house_type').xpath('a[1]/text()').extract()
            item['address'] = sel.css('.address').xpath('a[1]/@title').extract()[0]
            price = sel.css('.nhouse_price').xpath('span[1]/text()').extract()[0]
            try:
                item['price'] = int(price)
            except:
                item['price'] = 99999
            yield item            