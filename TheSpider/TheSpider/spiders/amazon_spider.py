import scrapy
from ..items import AmazonItem


class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    page_number = 2
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

        next_page = 'https://www.amazon.com/Books-Last-30-days/s?i=stripbooks&rh=n%3A283155%2Cp_n_publication_date' \
                    '%3A1250226011&page='+str(AmazonSpider.page_number)+'&qid=1575487589&ref=sr_pg_2 '
        if AmazonSpider.page_number < 10:
            AmazonSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)

