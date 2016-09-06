import scrapy


class StockItem(scrapy.Item):
    date = scrapy.Field()
    close = scrapy.Field()
    volume = scrapy.Field()