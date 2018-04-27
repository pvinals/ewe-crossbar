###############################################################################
##
##  Copyright (C) 2014, Tavendo GmbH and/or collaborators. All rights reserved.
##
##  Redistribution and use in source and binary forms, with or without
##  modification, are permitted provided that the following conditions are met:
##
##  1. Redistributions of source code must retain the above copyright notice,
##     this list of conditions and the following disclaimer.
##
##  2. Redistributions in binary form must reproduce the above copyright notice,
##     this list of conditions and the following disclaimer in the documentation
##     and/or other materials provided with the distribution.
##
##  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
##  AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
##  IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
##  ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
##  LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
##  CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
##  SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
##  INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
##  CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
##  ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
##  POSSIBILITY OF SUCH DAMAGE.
##
###############################################################################

from twisted.internet.defer import inlineCallbacks
from twisted.logger import Logger

from autobahn.twisted.util import sleep
from autobahn.twisted.wamp import ApplicationSession
from autobahn.wamp.exception import ApplicationError
from twisted.internet.defer import inlineCallbacks
from autobahn.wamp.interfaces import IPayloadCodec

from autobahn.wamp.types import PublishOptions, SubscribeOptions,EncodedPayload

import struct
import binascii

import sys
import subprocess


import n3Helper
import validatorParams
from voluptuous import MultipleInvalid
from elasticsearch import Elasticsearch


import pytest

import requests
import json
import os

  
class AppSession(ApplicationSession):

    log = Logger()
    
    n3Helper = n3Helper.N3Helper()
    
    elasticSearchID = 0
    
    url = "http://ewetasker.cluster.gsi.dit.upm.es/api/events"
    
    try:
        es = Elasticsearch(hosts=[{'host': os.environ['ES_ENDPOINT'], 'port': os.environ['ES_ENDPOINT_PORT']}])
        connected = es.ping()
        log.info("Correctly connected to elasticsearch: {connected}", connected = connected)
    except Error as e:
        log.info("Error connecting to elasticsearch: {e} ", e=e)
        


    @inlineCallbacks
    def onJoin(self, details):
        self.log.info("Connection details: {details}", details=details)
        
        def printParams(topic, args, kwargs):
            self.log.info("Args and kwargs for {topic}:", topic = topic)
            self.log.info("args received: {msg}", msg=args)
            self.log.info("kwargs received: {msg}", msg=kwargs)

        ## Resgistration to topic onEvent
        ##
        def onEvent(*args, **kwargs):
            
            printParams("com.channel.event", args, kwargs)
            
            try:
                #Deberiamos de validar aqui los kwargs
                validatorParams.verify(kwargs)
            except MultipleInvalid as e:
                self.log.info("Error Thrown while verifying json: {e}" , e = e)
                return e
            
            self.elasticSearchID = self.elasticSearchID+1
            kwargs['eventId'] = self.elasticSearchID
            kwargsTest = json.dumps(kwargs)
            self.log.info("Trying to load to elasticsearch: {event}", event = kwargsTest)
            res = self.es.index(index='crossbar', doc_type='events', id=self.elasticSearchID, body=kwargsTest)
            
            self.log.info("Loaded to elasticsearch: {event} - with id {esID}", event = kwargs, esID = self.elasticSearchID)
            
            eventn3Presence = self.n3Helper.getEvent(kwargs)
            
            
            payloadPresence = {"user": kwargs["user"],"inputEvent": eventn3Presence}
            
            self.log.info('The payload: {payload} ', payload = payloadPresence)

            data_channelsPresence = requests.post(self.url, data=payloadPresence)
            
            self.log.info("This is the response: {event} \n\n", event = data_channelsPresence.json())
            return data_channelsPresence.json()
            
     
            
        sub = yield self.register(onEvent, u'com.channel.event')
        self.log.info("Subscribed to topic 'com.channel.event'")
        

