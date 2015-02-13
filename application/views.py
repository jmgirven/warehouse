# -*- coding: utf-8 -*-
"""
Amazon warehouse project
"""

from flask import make_response
from flask import render_template

from application import app
from application.model import Item


def show_main():                                                                
    """Show main page"""
    itemsQuery = Item.query().order(-Item.created)
    items = itemsQuery.fetch(100)

    return table_of_results(items)


def search(searchStr):                                                                
    """Search catagory"""
    itemsQuery = Item.query(Item.catagory==searchStr).order(-Item.created)
    items = itemsQuery.fetch(100)

    return table_of_results(items)


def table_of_results(items):
    response = '<html><body><h2>Items</h2><ul>'

    for item in items:
        response += '<li><span>%s</span> --- <span>&#163;%s</span></li>'\
                % (item.title, item.price)

    response += '</ul></body></html>'

    return response


def page_not_found():
    """Show error page"""
    response = make_response(
        render_template('error.html'))
    response.headers['Content-Type'] = 'text/html'
    return response


def page_exception():
    """Show error page"""
    response = make_response(
        render_template('error.html'))
    response.headers['Content-Type'] = 'text/html'
    return response
    
    
if __name__ == '__main__':
    app.run()


#
