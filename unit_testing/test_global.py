import pytest
import json
import requests


def test_EventoMalEscrito1():
    url = "http://127.0.0.1:8082/call"
    data = {}
    data['procedures'] = 'com.channel.wifi'
    data['kwargs'] = {
        "events" : "hello"
    }
    json_data = json.dumps(data)
    r = requests.post(url, data=json_data)
    code = r.status_code
    print(code)
    assert code == 400

def test_EventoMalEscrito2():
    url = "http://127.0.0.1:8082/call"
    data = {}
    data['procedures'] = 'com.channel.wifi'
    data['args'] = {}
    data['kwargsa'] = {
        "events" : "hello"
    }
    json_data = json.dumps(data)
    r = requests.post(url, data=json_data)
    code = r.status_code
    print(code)
    assert code == 400
    
def test_EventoMalEscrito3():
    url = "http://127.0.0.1:8082/call"
    data = {}
    data['procedures'] = 'com.channel.wifi'
    data['argsa'] = {}
    data['kwargs'] = {
        "events" : "hello"
    }
    json_data = json.dumps(data)
    r = requests.post(url, data=json_data)
    code = r.status_code
    print(code)
    assert code == 400

    
def test_BadURL():
    url = "http://127.0.0.1:8082/publish"
    data = {}
    data['procedure'] = 'com.channel.wifi'
    data['kwargs'] = {
        "event" : "TurnON"
    }
    json_data = json.dumps(data)
    r = requests.post(url, data=json_data)
    code = r.status_code
    print(code)
    assert code == 400
    
def test_BadURL():
    url = "http://127.0.0.1:8088/call"
    data = {}
    data['procedure'] = 'com.channel.event'
    data['kwargs'] = {
        "event" : "TurnON"
    }
    json_data = json.dumps(data)
    variable = False
    try:
        r = requests.post(url, data=json_data)
    except:
        variable = True
    
    assert variable
    
def test_AllOK1():
    url = "http://127.0.0.1:8082/call"
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
    url = "http://127.0.0.1:8082/call"
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