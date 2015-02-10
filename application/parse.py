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

URL = "http://www.amazon.co.uk/s/?me=A2OAJ7377F756P&rh=i%3Amerchants%2Cn%3A429892031&rw_html_to_wsrp=1"

def parse_sites():                                                                
    """Parse sites"""
    req = urllib2.Request(URL)
    req.add_header('User-agent', 'Mozilla/5.0\
 (Windows NT 6.2; WOW64) AppleWebKit/537.11 (KHTML, like Gecko)\
 Chrome/23.0.1271.97 Safari/537.11')
    response = urllib2.urlopen(req)
    html = response.read()
    
    soup = BeautifulSoup(html)
    
    ul = soup.find("ul", id="s-results-list-atf")
    for li in ul.find_all('li'):
        title = li.find("h2", "s-access-title").text
        spans = li.find_all("span", "a-color-price")
        price = spans[0].text

        item = Item(
                title=title,
                price=convert_price(price)
            )
        item.put()

        logging.info("Item created: %s" % ( item.title))


    return html


def convert_price(price):
    """Convert a price"""
    if price[0] == u'\xa3':
        return float(price[1:])

    return float(price)

