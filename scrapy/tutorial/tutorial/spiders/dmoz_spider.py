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
    # self define
    page_num = 0
    def __init__(self):
      print 1
      self.file = open('records', 'w')
    def __del__(self):
      print 2
      self.file.close()
    def parse(self, response):
        full_url = self.start_urls[0]
        yield scrapy.Request(full_url, callback=self.parse_question)
    def parse_question(self, response):
        if self.page_num == 100:
          return
        self.page_num += 1
        sel = Selector(response)
        items = sel.xpath('//td/a/text()').extract()
        for item in items:
          print item.encode('utf-8')
          self.file.write(item.encode('utf-8') + '\n')
        next_page = sel.xpath('//a[@class="next"]/@href').extract()
        full_url = response.urljoin(next_page[0])
        yield scrapy.Request(full_url, callback=self.parse_question)
