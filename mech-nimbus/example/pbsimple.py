from twisted.spread import pb
from twisted.internet import app
class Echoer(pb.Root):
    def remote_echo(self, st):
        print 'echoing:', st
        return st
if __name__ == '__main__':
    appl = app.Application("pbsimple")
    appl.listenTCP(8789, pb.BrokerFactory(Echoer()))
    appl.run()