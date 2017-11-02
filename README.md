# PyEventSys
Easy-to-use and robust event system. Compatible with Python 3.5 (guaranteed), and maybe (untested) Python 3.4, 3.3 and 3.2.

## Installation
Download this repo as ZIP and extract the `eventsys.py` file to `<Python installdir>/Lib/site-packages`. No additional steps are required. Too easy to make a `setup.py`.

## API
------------------------
class `EventController`  
  The event controller. Create one to start actually using this event system.  
  
  `attach_handler(func, eventtype)`  
    Attach a handler to the specified event. func is the handler. eventtype is the event type name (string). Warns with HandlerAlreadyAttachedWarning if the specified event already has a handler.  
    
  `create_event(eventtype, \*args)`  
    Add event of type eventtype and arguments \*args to the event queue.  

-------------------------

decorator `attach_handler(controller, eventtype)`  
  A decorator for attaching handlers on fly. controller is the controller to attach the function to. eventtype is the same as for `EventController.attach_handler` and the warning is also applied. ***NOTE:*** The function does NOT "survive" after decorating so it will become None if it is applied with the `@` decorating syntax.

## Example

    import eventsys as evts # import eventsys
    
    contr = evts.EventController() # create a Controller. It controls the eventsys workflow - has a queue and a handlerdict.
    
    @evts.attach_handler(contr, 'event') # decorate our function
    def sayhello(somearg): # this is just an example
        print('Hello %s!' %somearg)
    
    contr.create_event('event', 'World') # add our example event to the queue
    contr.process_queue() # handle all events in the queue in FIFO sequence (well, because that's a QUEUE...)

This example will output `Hello World!`. ***NOTE:*** when creating games, use a subthread which calls `process_queue()` in a `while True` loop.
