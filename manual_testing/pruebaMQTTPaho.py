import paho.mqtt.client as mqtt
import struct, os, binascii, json


def dict_to_binary(the_dict):
    str = json.dumps(the_dict)
    binary = ' '.join(format(ord(letter), 'b') for letter in str)
    return binary

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    print("Connected with data "+str(userdata))
    print("Connected with client "+str(client._client_id))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
#    client.subscribe("$SYS/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client(client_id="test")
client.on_connect = on_connect
client.on_message = on_message

client.connect("127.0.0.1", 1883, 60)


topic = "com/example/testing"

obj = {
    "kwargs" : {
        "channel" : client._client_id.decode("utf-8"),
        "event" : "EventStart",
        "params" : {
            "eventTitle" : "Hello"
        }
    }
}
#test = json.dumps(obj)
binary = dict_to_binary(obj)
#payload = binascii.b2a_hex(test)

client.publish(topic, payload=binary, qos=0, retain=False)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()