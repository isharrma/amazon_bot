import scrapy
from ..items import AmazonBotItem


class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon_spider'
    start_urls = ['https://www.amazon.in/s?k=books&ref=nb_sb_noss_2']

    def parse(self, response):
        items = AmazonBotItem()

        #.extract() = .getall()
        book_name = response.css('.a-size-medium::text').extract()            
        book_author = response.css('.sg-col-12-of-28 .a-size-base+ .a-size-base').css('::text').extract() 
        book_price = response.css('.sg-col-20-of-28 .a-spacing-top-small .a-price-whole').css('::text').extract()
            #extra css as the above are using multiple html classes to extract 
        imagelink = response.css('.s-image-fixed-height .s-image').css('::attr(src)').extract()

        items['book_name'] = book_name
        items['book_author'] = book_author
        items['book_price'] = book_price
        items['imagelink'] = imagelink


        yield items
