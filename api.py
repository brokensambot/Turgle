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
import os
from google.appengine.ext.webapp.util import run_wsgi_app
from django.utils import simplejson
from google.appengine.ext.webapp import template
from datetime import timedelta
from google.appengine.ext import webapp

class Question(db.Model):
    date = db.DateTimeProperty(auto_now_add=True)
    text = db.TextProperty()
    hit_id = db.StringProperty()

class QuestionHandler(webapp.RequestHandler):
    # This URL should not handle GET requests.
    def get(self):
        self.error(405)
    
    def post(self):
        access_key = self.request.get(argument_name='accessKey', default_value=None)
        secret_key = self.request.get(argument_name='secretKey', default_value=None)
        answers_limit = self.request.get(argument_name='answersLimit', default_value=None)
        text = self.request.get(argument_name='text', default_value=None)
        if access_key == None or secret_key == None or answers_limit == None or text == None:
            self.error(400)
            return
        
        entity = Question(text=text)
        entity.put()
        
        connection = MTurkConnection(aws_access_key_id=access_key,
                                     aws_secret_access_key=secret_key,
                                     host='mechanicalturk.sandbox.amazonaws.com')
        question = ExternalQuestion('http://www.turgleapi.com/api/hit?questionId=' + str(entity.key().id()),
                                    300)
        result_set = connection.create_hit(question=question,
                                           lifetime=timedelta(minutes=90),
                                           max_assignments=answers_limit,
                                           title='Answer A Simple Question',
                                           description='Can you answer a simple question for me?',
                                           keywords='question, simple',
                                           reward=0.01,
                                           duration=timedelta(minutes=9),
                                           approval_delay=timedelta(days=3))
        try:
            for hit in result_set:
                entity.hit_id = hit.HITId
                entity.put()
        except:
            self.error(500)
            return
        
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(simplejson.dumps({'questionId': entity.key().id()}, indent=4))

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
        question_id = self.request.get(argument_name='questionId', default_value=None)
        if question_id == None:
            self.error(400)
            return
        
        question = Question.get_by_id(ids=int(question_id))
        if question == None:
            self.error(404)
            return
        
        path = os.path.join(os.path.dirname(__file__), 'templates')
        path = os.path.join(path, 'hit.html')
        self.response.out.write(template.render(path, {'text': question.text}))
    
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
