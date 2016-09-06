import scrapy


class NewsItem(scrapy.Item):
    date = scrapy.Field()
    title = scrapy.Field()
    description = scrapy.Field()