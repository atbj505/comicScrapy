#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import lxml.html
import pprint

LOGIN_URL = 'http://example.webscraping.com/places/default/user/login?_next=/places/default/index'
LOGIN_EMAIL = 'example@webscraping.com'
LOGIN_PASSWORD = 'example'


def parse_form(url):
    request = requests.get(url)
    html = request.text
    data = {}
    tree = lxml.html.fromstring(html)
    for e in tree.cssselect('form input'):
        if e.get('name'):
            data[e.get('name')] = e.get('value')
    return data


def login():
    login_request = requests.get(LOGIN_URL)
    params = {'email': LOGIN_EMAIL, 'password': LOGIN_PASSWORD}
    request = requests.post(
        LOGIN_URL, data=params, cookies=login_request.cookies)
    pprint.pprint(request.url)


def main():
    #     data = parse_form(LOGIN_URL)
    #     pprint.pprint(data)
    login()


if __name__ == "__main__":
    import pdb; pdb.set_trace()  # XXX BREAKPOINT
    main()
