#coding: utf-8

import scrapy
from scrapy.selector import Selector
import re

domain = 'http://bbs.hupu.com'
section = 'bxj'

class DmozSpider(scrapy.Spider):
    name = 'dmoz'
    allowed_domains = ['hupu.com']
    start_urls = [
        domain + '/' + section,
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
        if self.page_num == 1:
          return
        self.page_num += 1
        yield scrapy.Request('http://bbs.hupu.com/14535249.html', callback=self.parse_content)
        #for sel in response.xpath('//td[@class="p_title"]/a'):
        #   titles = sel.xpath('text()').extract()
        #   links =  sel.xpath('@href').extract()
        #   #if len(titles) != 1:
        #   if not titles:
        #     continue
        #   title = titles[0].encode('utf-8')
        #   #if re.search(r'专科', title) is None:
        #   #  continue
        #   link = domain + links[0]
        #   #self.file.write(title + '\n')
        #   #self.file.write(link + '\n')
        #   yield scrapy.Request(link, callback=self.parse_content)
        #next_page = response.xpath('//a[@class="next"]/@href').extract()
        #full_url = response.urljoin(next_page[0])
        #yield scrapy.Request(full_url, callback=self.parse_question)
    # content
    def parse_content(self, response):
        #for sel in response.xpath('//div[@class="author"]/div[@class="left"]/a'):
        for sel in response.xpath('//div[@class="floor_box"]'):
          author = sel.xpath('.//div[@class="author"]/div[@class="left"]/a/text()').extract_first().encode('utf-8')
          if not re.search(r'老九', author):
            continue
          contents = sel.xpath('.//tr/td/text()').extract()
          for index, content in enumerate(contents):
            print index, content.encode('utf-8')
            self.write(content.encode('utf-8'))
        next_page = response.xpath('//a[@class="next"]/@href').extract()
        if not next_page:
          return
        full_url = response.urljoin(next_page[0])
        yield scrapy.Request(full_url, callback=self.parse_content)

    def write(self, content):
        content = content.replace('\n','')
        self.file.write(content + '\n')
