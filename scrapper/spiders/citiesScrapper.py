# -*- coding: utf-8 -*-
import scrapy
from urls import urls

class cityPaginationSpider(scrapy.Spider):
	name = "CityScrapper"
	start_urls = urls
	
	def parse(self, response):
		document = response.xpath('//div[@id="dcmcontent"]/div[@class="lefttext"]')
		cities = document.xpath('//div[@class="DCColumn1p"]')
		for city in cities:
			type = city.xpath('img[contains(@title)]/@title').extract_first()
			name = city.xpath('a[contains(@title)]/@title').extract_first()
			adress = city.xpath('text()')
			
			yield {
				'name': name,
				'type': type,
				'adress': adress
			}