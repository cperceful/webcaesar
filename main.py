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
import caesar;
import cgi;

def buildPage(text = "", rot = ""):
    content = """
        <h1>Web Caesar</h1>
        <h3>Enter text to encrypt</h3>
        <form method="post">
            <textarea name="text" style="height: 100px; width: 300px">{}</textarea>
            <br>
            <h3>Enter rotation amount</h3>
            <input type="number" name="rot" value="{}">
            <input type="submit"/>
        </form>
    """.format(text, rot);

    return content;

class MainHandler(webapp2.RequestHandler):
    def get(self):

        content = buildPage();
        self.response.write(content);

    def post(self):
        text = self.request.get("text");
        rot = int(self.request.get("rot"));
        result = caesar.encrypt(text, rot);
        escapedResult = cgi.escape(result);

        content = buildPage(escapedResult, rot);
        self.response.write(content);

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
