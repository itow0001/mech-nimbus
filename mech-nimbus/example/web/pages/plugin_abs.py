from abc import ABCMeta, abstractmethod
from twisted.web.resource import Resource

class PluggableMeta(type):
    """ This class demos using a metaclass to register objects to be used in a dictionary
    dynamically
    """
    def __init__(cls, name, bases, dct):
        if not hasattr(cls, 'registry'):
            # this is the base class.  Create an empty registry
            cls.registry = {}
        else:
            # this is a derived class.  Add cls to the registry
            interface_id = name
            cls.registry[interface_id] = cls  
        super(PluggableMeta, cls).__init__(name, bases, dct)
        
        
class Pluggable(object):
    __metaclass__ = PluggableMeta
    
    
class FirstInterface(Pluggable,Resource):
    def echo(self):
        print "HELLO THIS IS THE FIRST INTERFACE" 
        
class SecondInterface(Pluggable,Resource):
    #name = "name is here"
    def __init__(self):
        pass
        self.name = "name is here"
    
    def set_name(self,value):
        self.name = value
        
    def echo(self, value = "HELLO THIS IS THE SECOND INTERFACE"):
        print value
        self.name = value


#print(Pluggable.registry)
# call as plugin class stored in registry
print Pluggable.registry.get("SecondInterface")().name

obj = Pluggable.registry.get("SecondInterface")
print obj()
obj().name = "Apple Zombie"
print obj().name 
#Pluggable.registry.get("SecondInterface")().name = "APPLE ZOMBIE"


print Pluggable.registry.get("SecondInterface")().name

