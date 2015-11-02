#!/usr/bin/env python
from __future__ import division
from random import randint

Users = [
    {
        'name': 'Cihat OGE',
        'Time': 100,
        'Report': 70,
    },
    {
        'name': 'Kadir Cetinkaya',
        'Time': 95,
        'Report': 70,
    },
    {
        'name': 'Mert Arisoy',
        'Time': 90,
        'Report': 90,
    },
    {
        'name': 'Omer Citak',
        'Time': 85,
        'Report': 80,
    },
    {
        'name': 'Evren Yalcin',
        'Time': 80,
        'Report': 85,
    },
    {
        'name': 'Oguzhan Uzman',
        'Time': 75,
        'Report': 70,
    },
    {
        'name': 'Deniz Parlak',
        'Time': 70,
        'Report': 70,
    },
    {
        'name': 'Harun Gulec',
        'Time': 65,
        'Report': 75,
    },
    {
        'name': 'Arjen Kilic',
        'Time': 60,
        'Report': 80,
    },
    {
        'name': 'Robin Dimyanoglu',
        'Time': 55,
        'Report': 85,
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
