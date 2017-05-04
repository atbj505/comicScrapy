# coding:utf-8

import scrapy
from bs4 import BeautifulSoup


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
        content = response.body
        soup = BeautifulSoup(content, "html5lib")
        listcon_tag = soup.find('ul', class_='listcon')
        com_a_list = listcon_tag.find_all('a', attrs={'href': True})

        comics_url_list = []
        base = 'http://www.xeall.com'
        for tag_a in com_a_list:
            url = base + tag_a['href']
            self.log(url)
            comics_url_list.append(url)
