from warnings import warn

__doc__ = \
"""
Easy-to-use and robust event system.
"""

class HandlerAlreadyAttachedWarning(Warning): # Warned if you attach a handler to a event which already has a handler
    pass
class NoHandlerAttachedWarning(Warning): # Warned if you push an event which does not have a handler
    pass
class NothingHappenedWarning(Warning): # Warned when an event without a handler is processed
    pass

class Event: # Yes, really, do not use it
    """
    DO NOT USE DIRECTLY
    """
    def __init__(self, eventtype, eventattrs):
        self.eventtype = eventtype
        self.eventattrs = eventattrs
    
    def __repr__(self):
        return '<%s Event with attrs %s @ %s>' %(self.eventtype, repr(self.eventattrs), hex(id(self)))

class EventController: # Use this one. Create one, attach handlers and push events!
    def __init__(self):
        self.queue = []
        self.handlers = {}
    
    def process_queue(self): # "Executes" all pushed events.
        for i in range(len(self.queue)):
            if self.queue[0].eventtype in range(len(self.handlers.keys())):
                self.handlers[self.queue[0].eventtype](*self.queue[0].eventattrs)
            else:
                warn('Event "%s" with index %s was ignored' %(self.queue[i].eventtype, i), NothingHappenedWarning)
            del self.queue[0]
    
    def attach_handler(self, func, eventtype):
        if eventtype in self.handlers.keys():
            warn('Handler is already attached, overwriting it', HandlerAlreadyAttachedWarning) # warn about overwriting event handler
        self.handlers[eventtype] = func
    
    def create_event(self, eventtype, *attrs):
        if not eventtype in self.handlers.keys():
            warn('This event will be ignored because it has no handler', NoHandlerAttachedWarning)
        self.queue.append(Event(eventtype, attrs))

def attach_handler(controller, eventtype):
    def wrap(func):
        controller.attach_handler(func, eventtype)
        return func
    return wrap
