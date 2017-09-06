#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver


def main():
    driver = webdriver.Chrome()
    driver.get('http://example.webscraping.com/places/default/search')
    driver.find_element_by_id('search_term').send_keys('.')
    js = "document.getElementById('page_size').options[1].text='1000'"
    driver.execute_script(js)
    driver.find_element_by_id('search').click()
    driver.implicitly_wait(30)

    links = driver.find_elements_by_css_selector('#results a')
    countries = [link.text for link in links]
    print(countries)

def vpn_test():
    # driver = webdriver.PhantomJS(executable_path = './phantomjs')
    driver = webdriver.PhantomJS()
    driver.get('http://www.site-digger.com/html/articles/20110516/proxieslist.html')
    trs = driver.find_elements_by_tag_name('tr')

    for tr in trs:
        # print(tr.text)
        print(tr.text.split(' ')[0])

if __name__ == "__main__":
    # main()
    vpn_test()
