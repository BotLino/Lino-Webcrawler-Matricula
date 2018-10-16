# -*- coding: utf-8 -*-
import scrapy
from crawler.items import CrawlerItem


class MatriculaSpider(scrapy.Spider):
    name = 'Matricula'
    allowed_domains = ['saa.unb.br']
    start_urls = ['http://www.saa.unb.br/graduacao/62-calendario-de-matricula']