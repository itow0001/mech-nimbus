from twisted.spread import pb
from twisted.internet import reactor
def gotObject(object):
    print "got object:",object
    object.callRemote("echo", "hello network").addCallback(gotEcho)
def gotEcho(echo):
    print 'server echoed:',echo
    reactor.stop()
def gotNoObject(reason):
    print "no object:",reason
    reactor.stop()
pb.getObjectAt("localhost", 8789, 30).addCallbacks(gotObject, gotNoObject)
reactor.run()