#!/usr/bin/env python
# -*- coding: utf-8 -*-

import builtwith
import whois
import requests
import robotparser
from requests.exceptions import RequestException
import re
import urlparse
import datetime


def download(url, user_agent='wswp', proxy=None, num_retries=2):
    headers = {'User-agent': user_agent}
    if proxy:
        request = requests.get(url, headers, proxies=proxy)
    else:
        request = requests.get(url, headers)
    try:
        html = request.text
        request.raise_for_status()
    except RequestException as e:
        html = None
        print(num_retries)
        if num_retries > 0:
            if request.status_code >= 500 and request.status_code < 600:
                return download(url, user_agent, num_retries-1)
    return html


def link_crawler(seed_url, link_regex, agent='wswp', max_depth=2):
    crawl_queue = [seed_url]
    seen = {}
    while crawl_queue:
        url = crawl_queue.pop()
        robot = get_robot(url)
        if robot.can_fetch(agent, url):
            html = download(url, agent)
            print('Downloading:%s' % url)
            depth = seen.get(url)
            if depth != max_depth:
                for link in get_links(html):
                    if re.match(link_regex, link):
                        link = urlparse.urljoin(seed_url, link)
                        if link not in seen:
                            seen[link] = depth + 1
                            crawl_queue.append(link)
        else:
            return

def get_links(html):
    webpage_regex = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
    return webpage_regex.findall(html)


def get_robot(url):
    rp = robotparser.RobotFileParser()
    rp.set_url(urlparse.urljoin(url, '/robots.txt'))
    rp.read()
    return rp

class Throttle(object):

    """Docstring for Throttle. """

    def __init__(self, delay):
       self.delay = delay
       self.domains = {}

    def wait(self, url):
        domain = urlparse.urlparse(url).netloc
        last_accessed = self.domains.get(domain)

        if self.delay > 0 and last_accessed is not None:
            sleep_secs = self.delay - (datetime.datetime.now() -
                                       last_accessed).seconds
            if sleep_secs > 0:
                time.sleep(sleep_secs)
        self.domains[domains] = datetime.datetime.now()


if __name__ == '__main__':
    # rp = robotparser.RobotFileParser(url='http://www.baidu.com/robots.txt')
    # rp.read()
    # url = 'http://www.baidu.com'
    # print(rp.can_fetch('Baiduspider', url))
    # print(builtwith.parse('http://www.idengyun.com'))
    # print(whois.whois('http://www.idengyun.com'))
    # html = download('https://httpstat.us/200')
    # print(html)
    seed_url = 'http://example.webscraping.com/index'
    link_regex = '/(index|view)'
    # link_crawler(seed_url, link_regex, max_depth=1)
    link_crawler(seed_url, link_regex, agent='BadCrawler')
