#coding: utf-8

import scrapy
from scrapy.selector import Selector

domain = "http://bbs.hupu.com"

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["hupu.com"]
    start_urls = [
        domain + "/bxj",
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
        if self.page_num == 20:
          return
        self.page_num += 1
        for sel in response.xpath('//td[@class="p_title"]/a'):
           #if len(sel.xpath('@href').re('/\d+.html')) != 0:
           titles = sel.xpath('text()').extract()
           links =  sel.xpath('@href').extract()
           if len(titles) != 1:
             continue
           title = titles[0].encode('utf-8')
           link = domain + links[0]
           self.file.write(title + '\n')
           self.file.write(link + '\n')
        next_page = response.xpath('//a[@class="next"]/@href').extract()
        full_url = response.urljoin(next_page[0])
        yield scrapy.Request(full_url, callback=self.parse_question)
