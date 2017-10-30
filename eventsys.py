from warnings import warn

__doc = \
"""
Easy-to-use and robust event system.
"""

class HandlerAlreadyAttachedWarning(Warning):
    pass

class NoHandlerAttachedWarning(Warning):
    pass

class Event:
    __doc__ = \
    """
    DO NOT USE DIRECTLY
    """
    def __init__(self, eventtype, eventattrs):
        self.eventtype = eventtype
        self.eventattrs = eventattrs
    
    def __repr__(self):
        return '<%s Event with attrs %s @ %s>' %(self.eventtype, repr(self.eventattrs), hex(id(self)))

class EventController:
    def __init__(self):
        self.queue = []
        self.handlers = {}
    
    def process_queue(self):
        for i in range(len(self.queue)):
            if self.queue[0].eventtype in self.handlers.keys():
                self.handlers[self.queue[0].eventtype](*self.queue[0].eventattrs)
            del self.queue[0]
    
    def attach_handler(self, func, eventtype):
        if eventtype in self.handlers.keys():
            warn(HandlerAlreadyAttachedWarning) # warn about overwriting event handler
        self.handlers[eventtype] = func
    
    def create_event(self, eventtype, *attrs):
        if not eventtype in self.handlers.keys():
            warn(NoHandlerAttachedWarning)
        self.queue.append(Event(eventtype, attrs))

def attach_handler(handler, eventtype):
    def wrap(func):
        handler.attach_handler(func, eventtype)
    return wrap
