import random
import string
import cherrypy

class StringGenerator(object):
    @cherrypy.expose
    def index(self):
        return """
        <HTML>
          <HEAD></HEAD>
          <BODY>
            <FORM method="get" action="generate">
              <INPUT type="text" value="8" name="length" />
              <BUTTON type="submit">Give it now!</BUTTON>
            </FORM>
          </BODY>
        </HTML>"""

    @cherrypy.expose
    def generate(self, length=8):
        some_string = ''.join(random.sample(string.hexdigits, int(length)))
        cherrypy.session['mystring'] = some_string
        return some_string
    
    @cherrypy.expose
    def display(self):
        return cherrypy.session['mystring']

if __name__ == '__main__':
    conf = {
        '/': {'tools.sessions.on': True}
    }
    cherrypy.quickstart(StringGenerator(), '/', conf)