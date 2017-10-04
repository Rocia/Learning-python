"""
A simple demo for using https://chain.so/api#realtime-balance-updates with Python.
"""


import pusherclient
import time
import json
import pprint
import logging
import sys
 
root = logging.getLogger()
root.setLevel(logging.INFO)
ch = logging.StreamHandler(sys.stdout)
root.addHandler(ch)
 
global pusher
 
 
def callback(data):
    data = json.loads(data)
    pprint.pprint(data)
 
 
def connect_handler(data):
    channel = pusher.subscribe('address_ltctest_muv26EP3gCTQAHq1vwCkVdMGRwXxqpE1mh')
    channel.bind('balance_update', callback)
    channel = pusher.subscribe('blockchain_update_ltctest')
    channel.bind('block_update', callback)
    channel.bind('tx_update', callback)
 
 
pusherclient.Pusher.host = "slanger1.chain.so"
pusher = pusherclient.Pusher('e9f5cc20074501ca7395', secure=True, log_level="DEBUG")
pusher.connection.bind('pusher:connection_established', connect_handler)
pusher.connect()
 
while True:
    time.sleep(1)
