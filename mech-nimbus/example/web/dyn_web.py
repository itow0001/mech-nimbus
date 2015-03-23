from twisted.web.server import Site
from twisted.web.resource import Resource
from twisted.internet import reactor

class Route(Resource):
    def __init__(self, path):
        Resource.__init__(self)
        self.path = path
        print "Page Fetch:%s" % (self.path)

    def render_GET(self, request):
        return "<html><body><pre>%s</pre></body></html>" % (self.path)
    

class PaymentRequired(Resource):  
    def render_GET(self, request):  
        request.setResponseCode(402)  
        return "<html><body>Please swipe your credit card.</body></html>"  


class init(Resource):
  def getChild(self, name, request):
      return Route(name)

root = init()
root.putChild("buy", PaymentRequired())
print root.listNames()
print root.listDynamicNames()
factory = Site(root)
reactor.listenTCP(8880, factory)
reactor.run()