import voluptuous
import objectpath, requests
import importlib
from voluptuous import Schema, Required, In, Object, Self, Exclusive, Inclusive, ALLOW_EXTRA


class Calendar:
    
    validate = Schema({
    Required('channel'): str, 
    Required('event'): str,
    Required("user"): str,
    Required('params'): {
        Required("eventTitle"): str 
    },
}, extra=ALLOW_EXTRA)
