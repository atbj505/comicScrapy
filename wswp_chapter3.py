#!/usr/bin/env python
# -*- coding: utf-8 -*-

import lxml
import requests

from PyQt5 import QtCore, QtGui
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication


def search_request(search_term, page_size=10, page=0):
    url = 'http://example.webscraping.com/places/ajax/search.json'
    params = {'search_term': search_term, 'page_size': page_size, 'page': page}
    result = requests.get(url, params=params)
    return result.json()


app = QApplication([])
webview = QWebEngineView()
loop = QtCore.QEventLoop()


def qt(url):
    webview.loadFinished.connect(loadFinished)
    webview.load(QtCore.QUrl(url))
    app.exec()
    webview.show()


def loadFinished(result):
    """TODO: Docstring for loadFinished.
    :returns: TODO
    """
    loop.quit()
    app.quit()
    print(result)
    html = webview.page().toHtml(callback)
    print(html)


def callback(html):
    print('callback')
    print(html)
    tree = lxml.html.fromstring(html)
    return tree.cssselect('#result')[0].text_content()


def main():
    #     json = search_request('c')
    # for countryInfo in json['records']:
        # print(countryInfo['country'])
    qt('http://example.webscraping.com/dynamic')


if __name__ == "__main__":
    main()


def render(source_html):
    """Fully render HTML, JavaScript and all."""

    import sys
    from PyQt5.QtCore import QEventLoop
    from PyQt5.QtWidgets import QApplication
    from PyQt5.QtWebEngineWidgets import QWebEngineView

    class Render(QWebEngineView):
        def __init__(self, html):
            self.html = None
            self.app = QApplication(sys.argv)
            QWebEngineView.__init__(self)
            self.loadFinished.connect(self._loadFinished)
            self.setHtml(html)
            while self.html is None:
                self.app.processEvents(QEventLoop.ExcludeUserInputEvents | QEventLoop.ExcludeSocketNotifiers | QEventLoop.WaitForMoreEvents)
            self.app.quit()

        def _callable(self, data):
            self.html = data

        def _loadFinished(self, result):
            self.page().toHtml(self._callable)

    return Render(source_html).html

import requests
sample_html = requests.get(dummy_url).text
print(render(sample_html))
