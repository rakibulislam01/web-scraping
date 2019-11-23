# -*- coding: utf-8 -*-
import scrapy


class ThespiderSpider(scrapy.Spider):
    name = 'thespider'
    allowed_domains = ['book.toscrape.com']
    start_urls = ['http://book.toscrape.com/']

    def parse(self, response):
        pass
