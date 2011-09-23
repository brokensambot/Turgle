#!/usr/bin/env python
#
# Copyright (c) 2011 Sam White
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

from google.appengine.ext import db
from boto.mturk.question import ExternalQuestion
from boto.mturk.connection import MTurkConnection
from google.appengine.ext.webapp.util import run_wsgi_app
from django.utils import simplejson
from google.appengine.ext import webapp

class Question(db.Model):
    date = db.DateTimeProperty(auto_now_add=True)
    text = db.TextProperty()

class QuestionHandler(webapp.RequestHandler):
    # This URL should not handle GET requests.
    def get(self):
        self.error(405)
    
    def post(self):
        accessKey = self.request.get(argument_name='accessKey', default_value=None)
        secretKey = self.request.get(argument_name='secretKey', default_value=None)
        answers = self.request.get(argument_name='answers', default_value=None)
        text = self.request.get(argument_name='text', default_value=None)
        if accessKey == None or secretKey == None or answers == None or text == None:
            self.error(400)
            return
        
        question = Question(text=text)
        question.put()
        
        # FIXME: Send the question to Mechanical Turk.
        
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(simplejson.dumps({'questionId': question.key().id()}, indent=4))

class AnswersHandler(webapp.RequestHandler):
    def get(self):
        # FIXME: Get the answers from Mechanical Turk.
        
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(simplejson.dumps({'answers': ['Red', 'Green', 'Blue']}, indent=4))
    
    # This URL should not handle POST requests.
    def post(self):
        self.error(405)

class HITHandler(webapp.RequestHandler):
    def get(self):
        questionId = self.request.get('questionId')
    
    # FIXME: Serve the HIT to Mechanical Turk.
    
    # This URL should not handle POST requests.
    def post(self):
        self.error(405)

def main():
    run_wsgi_app(webapp.WSGIApplication([('/api/question', QuestionHandler),
                                         ('/api/answers', AnswersHandler),
                                         ('/api/hit', HITHandler)],
                                        debug=True))

if __name__ == '__main__':
    main()
