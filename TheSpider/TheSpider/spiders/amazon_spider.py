import scrapy
from ..items import AmazonItem


class QuotesSpider(scrapy.Spider):
    name = 'amazon'
    start_urls = [
        'https://www.amazon.com/Books-Last-30-days/s?rh=n%3A283155%2Cp_n_publication_date%3A1250226011'
    ]

    def parse(self, response):
        items = AmazonItem()

        product_name = response.css('.a-color-base.a-text-normal').css('::text').extract()
        product_author = response.css('.a-color-secondary .a-size-base+ .a-size-base').css('::text').extract()
        product_price = response.css('.a-spacing-top-small .a-price-whole').css('::text').extract()
        product_imagelink = response.css('.s-image::attr(src)').extract()

        items['product_name'] = product_name
        items['product_author'] = product_author  # get
        items['product_price'] = product_price  # get
        items['product_imagelink'] = product_imagelink

        yield items
