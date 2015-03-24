from twisted.web.server import Site
from twisted.web.resource import Resource
from twisted.internet import reactor
from plugin_abs import Pluggable

class gun(Pluggable):
    def __init__(self):
        Resource.__init__(self)

    def render_GET(self, request):
        return "<html><body><pre> THIS IS SECOND GUN </pre></body></html>"