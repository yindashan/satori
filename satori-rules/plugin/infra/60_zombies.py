#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import absolute_import

# -- stdlib --
import json
import os
import socket
import time

# -- third party --
# -- own --

# -- code --
endpoint = socket.gethostname()
ts = int(time.time())

l = os.listdir('/proc')
l = filter(str.isdigit, os.listdir('/proc'))
states = ''.join([open('/proc/%s/stat' % i).read().split()[2] for i in l])

rst = [{
    'metric': 'proc.zombies',
    'endpoint': endpoint,
    'timestamp': ts,
    'step': 60,
    'value': states.count('Z'),
}, {
    'metric': 'proc.uninterruptables',
    'endpoint': endpoint,
    'timestamp': ts,
    'step': 60,
    'value': states.count('D'),
}]

print json.dumps(rst)
