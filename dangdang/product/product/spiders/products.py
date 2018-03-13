# -*- coding: utf-8 -*-
import scrapy
from product.items import ProductItem
from scrapy.http import Request

#http://search.dangdang.com/?key=%BC%C6%CB%E3%BB%FA&act=input
#http://search.dangdang.com/?key=%BC%C6%CB%E3%BB%FA&act=input&page_index=2
#name:    '//a[@name="itemlist-title"]/@title'
#price:     '//span[@class="search_now_price"]/text()'
#author:       '//a[@dd_name="单品作者"]/@title'
#comnum:     '//a[@class="search_comment_num"]/text()' 
class ProductsSpider(scrapy.Spider):
    name = 'products'
    allowed_domains = ['dangdang.com']
    start_urls = ('http://search.dangdang.com/?key=%BC%C6%CB%E3%BB%FA&act=input&page_index=1.html')

    def parse(self, response):
        item = ProductItem()
        item['name'] = response.xpath('//a[@name="itemlist-title"]/@title'),extract()
        item['price'] = response.xpath('//span[@class="search_now_price"]/text()'),extract()
        item['author'] = response.xpath('//a[@dd_name="单品作者"]/@title'),extract()
        item['comnum'] = response.xpath( '//a[@class="search_comment_num"]/text()'),extract()
        yield item
        for i in range(1,76):
        	url = 'http://search.dangdang.com/?key=%BC%C6%CB%E3%BB%FA&act=input&page_index='+str(i)
        	yield Request(url,callback=self.parse)
