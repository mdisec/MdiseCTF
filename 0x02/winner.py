#!/usr/bin/env python
from __future__ import division
from random import randint

Users = [
    {
        'name': 'Halit Alptekin',
        'Time': 100,
        'Report': 60,
    },
    {
        'name': 'Kadir Cetinkaya',
        'Time': 95,
        'Report': 80,
    },
]


def chance():
    return randint(0, 20) / 2

for user in Users:
    user['Random'] = chance()
    user['Final'] = (user['Time']*25 + user['Report']*30) / 100 + user['Random']
    print user

seq = [x['Final'] for x in Users]
print "WINNER IS"
print max(Users, key=lambda x:x['Final'])
