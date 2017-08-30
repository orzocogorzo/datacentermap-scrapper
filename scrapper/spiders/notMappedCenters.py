# -*- coding: utf-8 -*-
import scrapy
from not_mapped_urls import urls
import time

class NotmappedcentersSpider(scrapy.Spider):
    name = "notMappedCenters"
    allowed_domains = ["http://www.datacentermap.com/ajax/notmapped.html"]
    start_urls = urls

    def parse(self, response):
		city = response.css('h3::text').extract_first()
		points = response.css('a.black')
		static_url = 'http://www.datacentermap.com'
		time.sleep(5)
		
		for point in points:
			url = static_url + point.xpath('@href').extract_first()
			name = point.xpath('text()').extract_first()
			
			yield {
				'city': city,
				'name': name,
				'url': url
			}
