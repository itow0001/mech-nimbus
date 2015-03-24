from twisted.web.server import Site
from twisted.web.resource import Resource
from twisted.internet import reactor

class example(Resource):
    def __init__(self):
        Resource.__init__(self)

    def render_GET(self, request):
        return "<html><body><pre> THIS IS AN EXAMPLE </pre></body></html>"
    
