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
