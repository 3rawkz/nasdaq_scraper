import scrapy
from nasdaq.stock_items import StockItem


class StockSpider(scrapy.Spider):
    name = "stock"
    allowed_domains = ["nasdaq.com"]

    start_urls = [
        "http://www.nasdaq.com/symbol/goog/historical/"
    ]

    def __init__(self, symbol=''):
        self.start_urls =[
            "http://www.nasdaq.com/symbol/%s/historical/" % symbol,
        ]

    def parse(self, response):
        stockItem = StockItem()
        for sel in response.xpath('//div[@id="historicalContainer"]/descendant::tbody/tr'):
            stockItem['date'] = map(unicode.strip, sel.xpath('td[1]/text()').extract())
            stockItem['close'] = map(unicode.strip, sel.xpath('td[5]/text()').extract())
            stockItem['volume'] = map(unicode.strip, sel.xpath('td[6]/text()').extract())
            yield stockItem
