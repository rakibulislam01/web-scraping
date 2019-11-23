# -*- coding: utf-8 -*-
# runserver :  'scrapy crawl thespider'
# save file in csv format : 'scrapy crawl thespider -o book.csv'
import scrapy

pages = int(input('How Many Pages Do You Want to Scrape: '))
dictonary = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}


class ThespiderSpider(scrapy.Spider):
    name = 'thespider'
    # allowed_domains = ['book.toscrape.com']
    start_urls = ['http://books.toscrape.com/catalogue/page-{}.html'.format(i + 1) for i in range(pages)]

    def parse(self, response):
        data = {}
        books = response.css('ol.row')
        for book in books:
            for b in book.css('article.product_pod'):
                data['Title'] = b.css('a::attr(title)').getall()
                data['Price'] = b.css('div.product_price p.price_color::text').getall()
                data['Stock'] = b.css('div.product_price p.instock.availability::text').getall()[1].strip()
                data['Star'] = b.css('p::attr(class)').getall()[0].split()[-1]
                data['Star'] = [v for k, v in dictonary.items() if k in data['Star']][0]
                yield data
