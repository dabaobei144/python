#coding: utf-8

import scrapy
from scrapy.selector import Selector

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["hupu.com"]
    start_urls = [
        "http://bbs.hupu.com/bxj/",
    ]
    def parse(self, response):
        sel = Selector(response)
        items = sel.xpath('//td/a/text()').extract()
        for item in items:
          print item.encode('utf-8')
        #print [item for item in sel.xpath('//a')]
