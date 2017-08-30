# -*- coding: utf-8 -*-
import scrapy
from usa_states import urls

class cityPaginationSpider(scrapy.Spider):
	name = "City2Pagination"
	start_urls = urls
	
	def parse(self, response):
		document = response.xpath('//div[@id="dcmcontent"]/div[@class="lefttext"]')
		column1 = document.xpath('//div[@class="column1"]')
		column2 = document.xpath('//div[@class="column2"]')
		column3 = document.xpath('//div[@class="column3"]')
		if len(column1.extract()) == 0 and len(column2.extract()) == 0 and len(column3.extract()) == 0:
			columns = []
		else:
			columns = [column1,column2,column3]
			print
			print 'columns exist!'
			print
		
		for col in columns:
			for url in col.xpath('a/@href').extract():
				print url
				yield {
					'URL': response.url + url.split('/')[3] + '/'
				}