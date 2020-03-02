# -*- coding: utf-8 -*-
import scrapy
import json
from Douyu.items import DouyuItem

class DouyuSpider(scrapy.Spider):
    name = 'douyu'
    allowed_domains = ['capi.douyucdn.cn']
    baseUrl = 'http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset='
    offset = 0
    start_urls = [baseUrl + str(offset)]

    def parse(self, response):
    	nickList = json.loads(response.text)['data']
    	if len(nickList) == 0:
    		return 

    	for nick in nickList:
    		item = DouyuItem()
    		item['imagLink'] = nick['vertical_src']
    		item['nickName'] = nick['nickname']
    		item['nickCity'] = nick['anchor_city']
    		yield item 

    	self.offset += 20
    	yield scrapy.Request(self.baseUrl+str(self.offset),
    						callback=self.parse)
