
class PluggableMeta(type):
    """ This class demos using a metaclass to register plugins
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
    
    def __init__(self):
        self.name = "null"
    
    def set_name(self,value):
        self.name = value
    
    
    
    
class FirstInterface(Pluggable):
    pass

        
class SecondInterface(Pluggable):
    pass


print Pluggable.registry
print "\n\n\n"
a = Pluggable.registry.get("SecondInterface")
b = Pluggable.registry.get("SecondInterface")()





