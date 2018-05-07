import pytest
import json
import requests


def test_EventoMalEscrito():
    url = "http://ewecrossbar.cluster.gsi.dit.upm.es/call"
    data = {}
    data['procedure'] = 'com.channel.event'
    data['kwargs'] = {
        "events" : "hello"
    }
    json_data = json.dumps(data)
    r = requests.post(url, data=json_data)
    code = r.json()['error']
    print(code)
    assert code == 'wamp.error.runtime_error'
    
#def test_EventNotKnown():
#    url = "http://127.0.0.1:8082/call"
#    data = {}
#    data['procedure'] = 'com.channel.event'
#    data['kwargs'] = {
#        "channel" : "bluetooth",
#        "event" : "ON",
#        "params" : {}
#    }
#    json_data = json.dumps(data)
#    r = requests.post(url, data=json_data)
#    code = r.json()['error']
#    print(code)
#    assert code == 'wamp.error.runtime_error'
    
def test_AllOK1():
    url = "http://ewecrossbar.cluster.gsi.dit.upm.es/call"
    data = {}
    data['procedure'] = 'com.channel.event'
    data['kwargs'] = {
        "user": "admin",
        "channel" : "bluetooth",
        "event": "ON",
        "params" : {}
    }
    json_data = json.dumps(data)
    r = requests.post(url, data=json_data)
    code = r.json()["args"][0]["success"]
    print(code)
    assert code == 1

def test_AllOK2():
    url = "http://ewecrossbar.cluster.gsi.dit.upm.es/call"
    data = {}
    data['procedure'] = 'com.channel.event'
    data['kwargs'] = {
        "user": "admin",
        "channel" : "bluetooth",
        "event" : "OFF",
        "params" : {}
    }
    json_data = json.dumps(data)
    r = requests.post(url, data=json_data)
    code = r.json()["args"][0]["success"]
    print(code)
    assert code == 1