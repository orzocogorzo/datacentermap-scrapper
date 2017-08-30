# -*- coding: utf-8 -*-
import scrapy
from profile_urls import urls
import time

class ProfilesinfoscraperSpider(scrapy.Spider):
    name = "ProfilesInfoScraper"
    allowed_domains = ["http://www.datacentermap.com"]
    start_urls = urls

    def parse(self, response):
		document = response.css('#dcmcontent').css('.lefttext')
		address = document.xpath('div/div[@class="vcard"]/div[@class="adr"]')
		
		title = document.xpath('h1/text()').extract_first()
		description = document.xpath('text()').extract()[2]
		business_name = address.css('.organization-name::text').extract_first()
		business_address = address.css('.organization-unit.extended-address::text').extract_first()
		street_address = address.css('.street-address::text').extract_first()
		postal_code = address.css('.postal-code::text').extract_first()
		locality = address.css('.locality::text').extract_first()
		region = address.css('.region::text').extract_first()
		country = address.css('.country-name::text').extract_first()
		
		time.sleep(5)
		
		yield {
			'title': title,
			'description': description,
			'name': business_name,
			'extend address': business_address,
			'postal code': postal_code,
			'locality': locality,
			'region': region,
			'country': country
		}