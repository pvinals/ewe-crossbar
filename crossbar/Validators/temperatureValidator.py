import voluptuous
import objectpath, requests
import importlib
from voluptuous import Schema, Required, In, Object, Self, Exclusive, Inclusive, ALLOW_EXTRA


class Temperature:
    
    validate = Schema({
    Required('channel'): str, 
    Required('event'): str,
    Required("user"): str,
    Required('params'): {
        Required("temperature"): str,  
        Required("sensorId"): str
    },
}, extra=ALLOW_EXTRA)
