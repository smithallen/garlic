# -*- coding: utf-8 -*-
# @Author: yujinlun
# @Date:   2016-08-25 14:10:27
# @Last Modified by:   yujinlun
# @Last Modified time: 2016-08-25 14:20:53

'''
what is crawler and how it works
'''
import urlparse
import urllib
from bs4 import BeautifulSoup

url = "http://www.wandoujia.com"
urls_to_visit = [url]
urls_visited = []

while len(urls_to_visit) > 0:
    try:
        url = urls_to_visit.pop(0)
        htmltext = urllib.urlopen(url).read()

        print "visiting url:{0}".format(url)
    except Exception, e:
        print "failed to visit url:{0}".format(url)

    soup = BeautifulSoup(htmltext, "html.parser")

    for tag in soup.find_all('a', href=True):
        href = urlparse.urljoin(url, tag["href"])

        if href not in urls_visited:
            urls_to_visit.append(href)

    urls_visited.append(url)
