import voluptuous
import objectpath, requests, sys
import importlib
from voluptuous import Schema, Required, In, Exclusive, Inclusive, ALLOW_EXTRA


channels = ["bluetooth", "presence", "wifi", "calendar", "telegram"]


url = "http://ewetasker.cluster.gsi.dit.upm.es/mobileConnectionHelper.php"
payload = {"command" : "getChannels"}       
        
#        def find_between( s, first, last ):
#            try:
#                start = s.index( first ) + len( first )
#                end = s.index( last, start )
#                return s[start:end]
#            except ValueError:
#                return ""


def class_for_name(module_name, class_name):
    # load the module, will raise ImportError if module cannot be loaded
    m = importlib.import_module("Validators."+module_name)
    # get the class, will raise AttributeError if class cannot be found
    c = getattr(m, class_name)
    return c


data_channels = requests.post(url, data=payload)

data = data_channels.json()

tree_obj = objectpath.Tree(data)

channel = list(tree_obj.execute("$.title"))

print(channel)


def verify(params):
    validate(params)
    class_for_name(params["channel"]+"Validator", params["channel"].capitalize()).validate(params)
    



#validate = Schema({
#   Required('channel'): In(channels), 
#   Required('event'): str,
#   Required('params'): {
#       Required("sensorID"): str,
#       Required("distance"): str
#   }
# })

validate = Schema({
    Required('channel'): In(channel), 
    Required('event'): str,
    Required("user"): str
}, extra=ALLOW_EXTRA)

params = {}
params["channel"] = "calendar" 
params["event"] = "Less"
params["user"] = "admin"
params["params"] = {
    "eventTitle" : "Hello"
}


verify(params)
#{
#    "channel" : "algo",
#    "event": "otro",
#    "params": {
#        "sensorID1": "02312",
#        "time" : "2"
#    }
#}
#
#print(validate(params))