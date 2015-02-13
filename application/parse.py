#!/usr/bin/python
"""
Parse amazon warehouse
"""

from bs4 import BeautifulSoup
import logging
import urllib2

from flask import make_response
from flask import redirect
from flask import url_for

from application import app
from application.model import Item

URL_PREFIXES = [\
        "http://www.amazon.co.uk/s/ref=sr_pg_2?me=A2OAJ7377F756P&rh=n%3A340831031%2Cn%3A%21340832031%2Cn%3A429892031&page=",\
        "http://www.amazon.co.uk/s/ref=sr_pg_2?me=A2OAJ7377F756P&rh=n%3A304072031%2Ck%3Askateboard&page="\
        ]
URL_SUFFIXES = [\
        "&ie=UTF8&qid=1423666390",\
        "&keywords=skateboard&ie=UTF8&qid=1423850007"\
        ]
CATAGORIES = [\
        "tablets",\
        "skateboards"\
        ]

def parse_sites():                                                                
    """Parse sites"""
    items = 0

    for iii in range(len(URL_PREFIXES)):
        URL_PREFIX = URL_PREFIXES[iii]
        URL_SUFFIX = URL_SUFFIXES[iii]
        CATAGORY = CATAGORIES[iii]

        page = 1

        while True:
            logging.info("Page: %s" % page)

            try:
                # Send request
                req = urllib2.Request(URL_PREFIX + str(page) + URL_SUFFIX)
                req.add_header('User-agent', 'Mozilla/5.0\
 (Wi            ndows NT 6.2; WOW64) AppleWebKit/537.11 (KHTML, like Gecko)\
 Chr            ome/23.0.1271.97 Safari/537.11')
                response = urllib2.urlopen(req)
                html = response.read()
                
                # Parse response
                soup = BeautifulSoup(html)

                # Check if we went passed the max pages
                currentPage = int(soup.find('span', 'pagnCur').text)
                if currentPage < page:
                    logging.info("Current page: %s" % currentPage)
                    break
           
                # Iterate through ul's and li's looking for items
                for ul in soup.find_all("ul", "s-result-list"):
                    for li in ul.find_all('li'):
                        # Grab info
                        title = li.find("h2", "s-access-title").text
                        spans = li.find_all("span", "a-color-price")
                        price = spans[0].text

                        # Save to DB
                        item = Item(
                                title=title,
                                price=convert_price(price),
                                catagory=CATAGORY
                            )
                        item.put()

                        items += 1

                        logging.info("Item created: %s" % ( item.title))

            except Exception as e:
                logging.info("Exception: %s" % e)

            page += 1


    return "Scanned %s pages, found %s items" % (page, items)


def convert_price(price):
    """Convert a price"""
    if price[0] == u'\xa3':
        return float(price[1:])

    return float(price)

