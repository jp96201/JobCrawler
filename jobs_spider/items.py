# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JobsSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    status = scrapy.Field()
    title = scrapy.Field()
    salary = scrapy.Field()
    city = scrapy.Field()
    exp = scrapy.Field()
    degree = scrapy.Field()
    description = scrapy.Field()
    pass
