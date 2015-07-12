__author__ = 'lishaohua'

from scrapy.spiders import CrawlSpider, Rule
from scrapy import FormRequest
from scrapy import Request, Item
from scrapy.linkextractor import LinkExtractor


class book3_spider(CrawlSpider):
    name = 'zgjd'
    allowed_domains = 'www.cssn.cn'

    rules = (
        Rule(
            LinkExtractor(), callback='parse_item'
        ),
        # Rule(
        # LinkExtractor(allow=('.*\./\d+/t\d+\.shtml', )), callback='parse_item'
        # ),
        # Rule(
        # LinkExtractor(allow=('.*index_\d*\.shtml', ))
        # ),
    )

    def start_requests(self):
        url_file = open('data/cssn_cn/book_list_one.txt')
        requests = []
        headders = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Cookie': 'wdcid=188046e62ef671c3; X-Mapping-fgoepopa=DE9E81ABB145F5B1E15E52EBEB1500DC; CNZZDATA5545901=cnzz_eid%3D363909646-1436623305-null%26ntime%3D1436683130; wdlast=1436684250',
            'Host': 'www.cssn.cn',
            'User-Agent': 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.125 Safari/537.36',
        }
        for url in url_file:
            request = Request(url=url[0:-1], headers=headders, cookies=True)
            requests.append(request)
        return requests


    def parse_item(self, response):
        self.log('>>>>>>>>>>>>>>>>>>>>Hi, this is an item page! %s ' % response.url)
        print('-===========================================')
        item = Item()
        # item['id'] = response.xpath('//td[@id="item_id"]/text()').re(r'ID: (\d+)')
        # item['name'] = response.xpath('//td[@id="item_name"]/text()').extract()
        # item['description'] = response.xpath('//td[@id="item_description"]/text()').extract()
        return item
