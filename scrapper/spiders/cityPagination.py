# -*- coding: utf-8 -*-
import scrapy
from urls import urls

class cityPaginationSpider(scrapy.Spider):
	name = "CityPagination"
	start_urls = urls
	
	def parse(self, response):
		document = response.xpath('//div[@id="dcmcontent"]/div[@class="lefttext"]')
		column1 = document.xpath('//div[@class="column1"]')
		column2 = document.xpath('//div[@class="column2"]')
		column3 = document.xpath('//div[@class="column3"]')
		columns = [column1,column2,column3]
		
		for col in columns:
			for url in col.xpath('a/@href').extract():
				yield {
					'URL': response.url + url.split('/')[2] + '/'
				}