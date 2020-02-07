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
        return ''.join(random.sample(string.hexdigits, int(length)))

if __name__ == '__main__':
    cherrypy.quickstart(StringGenerator())