import cherrypy

class HelloWorld:
    @cherrypy.expose
    def index(self):
        return "Hello world!"

if __name__ == '__main__':
    cherrypy.quickstart(HelloWorld())