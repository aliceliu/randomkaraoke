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
        song = get_song(self.request.get("song"))
        #related_song = get_related_song(base_song)
       
        template_values = {
                          #'song': song,
                          #'video_id': choice,
                          #'related_song': related_song,
                          'song': song
        }
        template = jinja_environment.get_template("home.html")
        self.response.out.write(template.render(template_values))
        
      

routes=[
  ('/', MainHandler),
]
app = webapp2.WSGIApplication(routes,
                              debug=True)


