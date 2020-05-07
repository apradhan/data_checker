import scrapy

class Dataset(scrapy.Item):
    name = scrapy.Field()
    link = scrapy.Field()
    organization = scrapy.Field()