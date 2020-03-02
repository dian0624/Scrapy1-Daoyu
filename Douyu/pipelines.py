# -*- coding: utf-8 -*-
from scrapy.pipelines.images import ImagesPipeline
import scrapy
class DouyuImagePipeline(ImagesPipeline):
	def get_media_requests(self,item,info):
		imageLink = item['imagLink']
		yield scrapy.Request(imageLink)
