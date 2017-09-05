#!/usr/bin/env python
# -*- coding: utf-8 -*-

from wswp_chapter1 import download
from bs4 import BeautifulSoup
import lxml.html
from pymongo import MongoClient

def scrape_callback(url, html):
    print('callBack')

if __name__ == "__main__":
    # url = 'http://example.webscraping.com/places/default/view/United-Kingdom-239'
    # html = download(url)
    # soup = BeautifulSoup(html)
    # tr = soup.find('tr', attrs={'id':'places_area__row'})
    # td = tr.find('td', attrs={'class':'w2p_fw'})
    # area = td.text

    # tree = lxml.html.fromstring(html)
    # td = tree.cssselect('tr#places_area__row > td.w2p_fw')[0]
    # area = td.text_content()
    # print(area)

    # client = MongoClient('localhost', 27017)
    # db = client.cache
    # db.webpage.insert({'url': url, 'html': html})
    # db.webpage.update({'_id': url}, {'$set': {'html': html}}, upsert=True)
    # print(db.webpage.find_one({'_id': url}))
    # print(db.webpage.find({'_id': url}).count())

    html = download('http://example.webscraping.com/places/default/search')
    tree = lxml.html.fromstring(html)
    print(tree.cssselect('div#results a'))
