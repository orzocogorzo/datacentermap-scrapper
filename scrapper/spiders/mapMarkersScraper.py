# -*- coding: utf-8 -*-
import scrapy
from map_urls import urls
import time
import os

class MapmarkersscraperSpider(scrapy.Spider):
    name = "mapMarkersScraper"
    allowed_domains = ["http://www.datacentermap.com/ajax/map.html"]
    start_urls = urls

    def parse(self, response):
		name = response.css('a h3::text').extract_first()
		id = response.url.split('=')[1].split('a')[0]
		static_url = "http://www.datacentermap.com"
		url = static_url + response.css('a::attr(href)').extract_first()
		time.sleep(5)
		yield {
			'name': name,
			'id': id,
			'url': url
		}