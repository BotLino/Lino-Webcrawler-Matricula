# -*- coding: utf-8 -*-
import scrapy
from crawler.items import CrawlerItem


class RegistrationSpider(scrapy.Spider):
    name = 'registration'
    allowed_domains = ['saa.unb.br']
    start_urls = ['http://www.saa.unb.br/graduacao/62-calendario-de-matricula']

    def parse(self, response):
        for element in response.css(".wrapper .grid-block .grid-box .grid-block .item .content p a"):
            path = element.css("a::attr(href)").extract_first()
            text = element.css("a::text").extract_first()
            
            if path and text:
                pdf = response.follow(path).url
                item = CrawlerItem(text=text, path=path, url=pdf)
                yield item