import re
import datetime
from scrapy.contrib.spiders import XMLFeedSpider
from nasdaq.news_items import NewsItem


class NewsSpider(XMLFeedSpider):
    name = "news"
    allowed_domains = ["nasdaq.com"]
    start_urls = [
        "http://articlefeeds.nasdaq.com/nasdaq/categories?category=Stocks",
        "http://articlefeeds.nasdaq.com/nasdaq/categories?category=Mutual+Funds"
    ]

    itertag = 'item'

    def parse_node(self, response, node):
        item = NewsItem()
        item['date'] = node.xpath('pubDate/text()').extract()
        item['title'] = node.xpath('title/text()').extract()

        # function that remove img tag from raw text
        def remove_img_tag(raw_text):
            clean_re = re.compile(r'<img.*?>')
            clean_text = re.sub(clean_re, '', raw_text)
            return clean_text

        # description with img tag removed
        desc = node.xpath('description/text()').extract()
        clean_desc = remove_img_tag(desc[0])
        item['description'] = clean_desc

        # sort by date
        date_item = item['date']
        item['date'] = sorted(date_item, key=lambda x: datetime.datetime.strptime(x, '%a, %d %b %Y %H:%M:%S -0400'))
        yield item
