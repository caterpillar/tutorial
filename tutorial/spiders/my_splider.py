__author__ = 'lishaohua'

import scrapy
from scrapy.selector import HtmlXPathSelector
from tutorial.items import Book


class MySpider(scrapy.Spider):
    name = 'gushiwen.org'
    allowed_domains = 'so.gushiwen.org/'
    start_urls = [
        'http://so.gushiwen.org/guwen/Default.aspx?p=1',
        'http://so.gushiwen.org/guwen/Default.aspx?p=2',
        'http://so.gushiwen.org/guwen/Default.aspx?p=3',
        'http://so.gushiwen.org/guwen/Default.aspx?p=4',
        'http://so.gushiwen.org/guwen/Default.aspx?p=5',
        'http://so.gushiwen.org/guwen/Default.aspx?p=6',
        'http://so.gushiwen.org/guwen/Default.aspx?p=7',
        'http://so.gushiwen.org/guwen/Default.aspx?p=8',
        'http://so.gushiwen.org/guwen/Default.aspx?p=9',
        'http://so.gushiwen.org/guwen/Default.aspx?p=10'
    ]


    def parse(self, response):
       # self.log('A response from %s just arrived!' % response.url)
        self.log(response)
        hxs = HtmlXPathSelector(response)
        books = hxs.xpath('//div[@class="sons"]')
        items = []
        for book in books:
            item = Book()
            item['name'] = book.xpath('p[@style="font-size:14px;"]/text()').extract()
            item['url'] = book.xpath('p[@style="font-size:14px;"]/@href').extract()
            item['author'] = book.xpath('p[@style="color:#676767;"]/text()').extract()
            items.append(item)
        return items

