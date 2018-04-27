import voluptuous
import objectpath, requests
import importlib
from voluptuous import Schema, Required, In, Object, Self, Exclusive, Inclusive


class Calendar:
    
    validate = Schema({
    Required('channel'): str, 
    Required('event'): str,
    Required("user"): str,
    Required('params'): {
        Required("eventTitle"): str 
    }
    })
