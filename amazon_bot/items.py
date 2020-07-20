# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonBotItem(scrapy.Item):
    book_name = scrapy.Field()
    book_author = scrapy.Field()
    book_price = scrapy.Field()
    imagelink = scrapy.Field()
    pass
