#!/usr/bin/python

import json
import subprocess
import re
import time
from cStringIO import StringIO
from jsonrpc import ServerProxy, JsonRpc20, TransportTcpIp
from pprint import pprint


class StanfordNLP:
    def __init__(self):
        self.server = ServerProxy(JsonRpc20(),
                                  TransportTcpIp(addr=("127.0.0.1", 8080)))
    
    def parse(self, text):
        return json.loads(self.server.parse(text))


nlp = StanfordNLP()
def parseText(text):
    return nlp.parse(text)
text = "The mother loves the daughter.  Joan knows that Bob wants to go to the beach that is sandy.  She asks if he wants a ride."

parseDict = parseText(text)
POS_Array = []
Dep_Array = []
for sentence in parseDict['sentences']:
    for dep in sentence['dependencies']:
	temp
	if "nsubj" in dep[0]:
	    
    for word in sentence['words']:
	POS_Array.append(word[1]['PartOfSpeech'])
print POS_Array
