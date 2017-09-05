#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import lxml
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWebEngineCore import *
from PyQt5.QtWebEngine import *

def search_request(search_term, page_size=10, page=0):
    url = 'http://example.webscraping.com/places/ajax/search.json'
    params = {'search_term': search_term, 'page_size': page_size, 'page': page}
    result = requests.get(url, params=params)
    return result.json()


def callback(html):
    print('callback')
    print(html)
    tree = lxml.html.fromstring(html)
    return tree.cssselect('#result')[0].text_content()


def qt(url):
    app = QApplication([])
    webview = QWebEngineView()
    loop = QtCore.QEventLoop()
    webview.loadFinished.connect(loop.quit)
    webview.load(QtCore.QUrl(url))
    loop.exec()
    webview.page().toHtml(callback)

def main():
#     json = search_request('c')
    # for countryInfo in json['records']:
        # print(countryInfo['country'])
    qt('http://example.webscraping.com/dynamic')

if __name__ == "__main__":
    main()
