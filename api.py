#!/usr/bin/env python

from boto.mturk.question import ExternalQuestion
from boto.mturk.connection import MTurkConnection
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import webapp

class QuestionHandler(webapp.RequestHandler):
    # This URL should not handle GET requests.
    def get(self):
        self.error(404)
    
    def post(self):
        self.response.headers['Content-Type'] = 'text/plain'

class AnswersHandler(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
    
    # This URL should not handle POST requests.
    def post(self):
        self.error(404)

def main():
    run_wsgi_app(webapp.WSGIApplication([('/api/question', QuestionHandler),
                                         ('/api/answers', AnswersHandler)],
                                        debug=True))

if __name__ == '__main__':
    main()
