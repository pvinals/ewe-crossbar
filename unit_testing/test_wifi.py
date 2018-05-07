import pytest
import json
import requests
import time




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
    
def test_EventNotKnown():
    url = "http://ewecrossbar.cluster.gsi.dit.upm.es/call"
    data = {}
    data['procedure'] = 'com.channel.event'
    data['kwargs'] = {
        "event" : "hello"
    }
    json_data = json.dumps(data)
    r = requests.post(url, data=json_data)
    code = r.json()['error']
    print(code)
    assert code == 'wamp.error.runtime_error'
    
def test_AllOK1():
    
    time.sleep(10)
    url = "http://ewecrossbar.cluster.gsi.dit.upm.es/call"
    data = {}
    data['procedure'] = 'com.channel.event'
    data['kwargs'] = {
        "user": "admin",
        "channel" : "wifi",
        "event": "OFF",
        "params" : {}
    }
    json_data = json.dumps(data)
    r = requests.post(url, data=json_data)
    code = r.json()["args"][0]["success"]
    print(code)
    assert code == 1

def test_AllOK2():
    time.sleep(2)
    url = "http://ewecrossbar.cluster.gsi.dit.upm.es/call"
    data = {}
    data['procedure'] = 'com.channel.event'
    data['kwargs'] = {
        "user": "admin",
        "channel" : "wifi",
        "event": "ON",
        "params" : {}
    }
    json_data = json.dumps(data)
    r = requests.post(url, data=json_data)
    code = r.json()["args"][0]["success"]
    print(code)
    assert code == 1