"""
urls.py

URL dispatch route mappings and error handlers

"""
from flask import render_template

from application import app

from application import parse
from application import views



## URL dispatch rules
# App Engine warm up handler
# See http://code.google.com/appengine/docs/python/config/appconfig.html#Warming_Requests
#app.add_url_rule('/_ah/warmup', 'warmup', view_func=views.warmup)

# Home page
app.add_url_rule('/', 'show_main', view_func=views.show_main)

# Home page
app.add_url_rule('/go', 'parse_sites', view_func=parse.parse_sites)


### Error handlers
## Handle 404 errors
#@app.errorhandler(404)
#def page_not_found(e):
#    """Return a custom 404 error."""
#    return views.page_not_found()
#
#
## Handle 500 errors
#@app.errorhandler(500)
#def page_exception(e):
#    """Return a custom 500 error."""
#    return views.page_exception()
