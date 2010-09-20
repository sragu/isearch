import bottle
from google.appengine.ext.webapp import util 

from bottle import route
@route('/')
@route('/index.html')
def index():
    return "Provides search suggestions. Try /suggest/<word>"

@route('/suggest/:keyword')
def suggest(keyword):
    return {'keyword': keyword , 'suggestions': _retrieve_suggestions(keyword)}

def _retrieve_suggestions(keyword):
	return "%s" % keyword

util.run_wsgi_app(bottle.default_app())

