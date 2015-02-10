# -*- coding: utf-8 -*-
"""
Amazon warehouse project
"""

from flask import make_response
from flask import render_template

from application import app



def show_main():                                                                
    """Show main page"""                                                        
    response = make_response(
        render_template('index.html'))
    response.headers['Content-Type'] = 'text/html'

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
