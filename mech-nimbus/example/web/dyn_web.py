""" This is a demo of dynamic routing to a dynamically loaded class:
* dynamic routing
* dynamically adding a class 
"""
from twisted.web.server import Site
from twisted.web.resource import Resource
from twisted.internet import reactor
import pkgutil
import os, sys

class default(Resource):
    """routes which don`t have a home go here
    """
    def __init__(self, path):
        Resource.__init__(self)
        self.path = path
        print "Page Fetch:%s" % (self.path)
    def render_GET(self, request):
        return "<html><body><pre>%s</pre></body></html>" % (self.path)

class Route(Resource):
    
    """This routes requests mapped to a python class which are dynamically loaded
    """
    def getChild(self, name, request):
        path = os.path.join(os.path.dirname(__file__), "pages")# location of mods
        modules = pkgutil.iter_modules(path=[path])# define package location
        for loader, mod_name, ispkg in modules:
            if mod_name == name and not mod_name == "Base":# module exists run it
                if mod_name not in sys.modules:# make sure its been loaded
                    loaded_mod = __import__(path+"."+mod_name, fromlist=[mod_name])
                    loaded_class = getattr(loaded_mod, mod_name)
                    instance = loaded_class()
                    return instance
        return default(name)

root = Route()
factory = Site(root)
reactor.listenTCP(8880, factory)
reactor.run()
