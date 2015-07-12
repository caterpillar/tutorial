# coding=utf-8
__author__ = 'lishaohua'


from scrapy.spider import Spider
from scrapy.selector import Selector
from tutorial.items import Book2


class MyBook2Spider(Spider):
    """
    抓取 中国社会科学网 经史子集数据 http://www.cssn.cn/sjxz/xsjdk/zgjd/
    """

    name = 'cssn.cn'
    allowed_domains = 'www.cssn.cn'
    start_urls = ['http://www.cssn.cn/sjxz/xsjdk/zgjd/']

    def parse(self, response):
        self.log('A response from %s just arrived!' % response.url)
        hxs = Selector(response)
        book_type1_list = hxs.xpath('//div[@class="mks-main2"]/div[@class="mks-main-topListTab"]')
        book_items = []
        open('data/cssn_cn/html_response/book_list.html', 'wr').write(response.body)
        book_url_file = open('data/cssn_cn/book_list2.txt', 'wr')
        for book_type1 in book_type1_list:
            book_type1_name = book_type1.xpath('div[@class="topListTab_title"]/p/a/text()').extract()
            book_type2_list = book_type1.xpath('//div[@class="topListTab_title_cenner"]')
            for book_type2 in book_type2_list:
                book_list = book_type2.xpath('div/ul/li')
                for book in book_list:
                    book2 = Book2()
                    book2['name'] = book.xpath('a/text()').extract()
                    book2['url'] = book.xpath('a/@href').extract()
                    book2['book_type1'] = book_type1_name
                    book_items.append(book2)
                    self.log(type(book2['url']))
                    if len(book2['url']) > 0:
                        book_url_file.write(book2['url'][0] + '\n')


        return book_items