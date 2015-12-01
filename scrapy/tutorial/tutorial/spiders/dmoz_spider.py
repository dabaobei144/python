#coding: utf-8

import scrapy
from scrapy.selector import Selector

domain = "http://bbs.hupu.com"

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["hupu.com"]
    start_urls = [
        domain + "/bxj/",
    ]
    def parse(self, response):
        page_num = 1
        sel = Selector(response)
        #items = sel.xpath('//td/a/text()').extract()
        #for item in items:
        #  print str(page_num) + ':\n' + item.encode('utf-8')
        #  print '\n'
        next_page = sel.xpath('//a[@class="next"]/@href').extract()
        full_url = response.urljoin(next_page[0])
        yield scrapy.Request(full_url, callback=self.parse_question)
    def parse_question(self, response):
        sel = Selector(response)
        items = sel.xpath('//td/a/text()').extract()
        for item in items:
          print item.encode('utf-8')
        next_page = sel.xpath('//a[@class="next"]/@href').extract()
        full_url = response.urljoin(next_page[0])
        yield scrapy.Request(full_url, callback=self.parse_question)
