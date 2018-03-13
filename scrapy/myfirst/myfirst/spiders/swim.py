# -*- coding: utf-8 -*-
import scrapy
from myfirst.items import MyfirstItem


class SwimSpider(scrapy.Spider):
    name = 'swim'
    allowed_domains = ['sina.com.cn']
    start_urls = (
    	'http://video.sina.com.cn/p/news/s/doc/2018-02-03/093867948391.html?cre=tianyi&mod=pchome&loc=0&r=-1&doct=0&rfunc=61&tj=none&tr=73',
    	'http://video.sina.com.cn/p/news/c/doc/2018-02-02/082767942377.html?cre=tianyi&mod=pchome&loc=2&r=25&doct=0&rfunc=61&tj=none&tr=25'
    )

    def parse(self, response):
        item =MyfirstItem()
        item["urlname"] = response.xpath("/html/head/title/text()")
        print(11)
        print(item["urlname"])
        print(12)
