# coding:utf-8

import scrapy


class Comics(scrapy.Spider):
    """
    漫画爬虫
    """

    name = "comics"

    def start_requests(self):
        urls = ['http://www.xeall.com/shenshi']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        self.log(response.body)
