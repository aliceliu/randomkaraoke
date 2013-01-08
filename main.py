#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import jinja2
import os
import logging
from randomkaraoke import *

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))


class MainHandler(webapp2.RequestHandler):
    def get(self):
        choice = self.request.get("choice")
        template_values = {}
        template = jinja_environment.get_template("home.html")
        self.response.out.write(template.render(template_values))


class KaraokeHandler(webapp2.RequestHandler):
    def get(self):
        choice = self.request.get("choice")
        if not choice:
            choice = 'never gonna give you up'
        while True:
            try:
                song = get_song(choice)
                break
            except:
                pass
        original_song = get_song(choice, original=True)
        related_song = get_related_song('http://www.youtube.com/watch?v=' + song)
       
        template_values = {
                          'choice': choice,
                          'song': song,
                          'original_song': original_song,
                          'related_song': related_song
        }
        template = jinja_environment.get_template("karaoke.html")
        self.response.out.write(template.render(template_values))
        

        
      

routes=[
  ('/', MainHandler),
  ('/sing', KaraokeHandler)
]
app = webapp2.WSGIApplication(routes,
                              debug=True)


