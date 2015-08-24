#!/usr/bin/env python
from __future__ import division
from random import randint

Users = [
    {
        'name': 'Ceylan Bozogullarindan',
        'Time': 100,
        'Report': 90,
    },
    {
        'name': 'Ali Agdeniz',
        'Time': 95,
        'Report': 70,
    },
    {
        'name': 'Hasan Emre Ozer',
        'Time': 90,
        'Report': 85,
    },
    {
        'name': 'Robin Daimyanoglu',
        'Time': 85,
        'Report': 100,
    }
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
