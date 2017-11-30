# -*- coding: utf-8 -*-
# trump-net (c) Ian Dennis Miller

from datetime import datetime
from situation import Event
from .persons import *
from .places import *

"""
Event.create(name="",
    place=,
    timestamp=datetime(, , , 0, 0, 0),
    actors=[
    ])
"""

Event.create(name="Trump Tower Meeting",
    place=trump_tower,
    actors=[
        donald_trump_jr,
        paul_manafort,
        jared_kushner,
        natalia_veselnetskaya,
    ])

Event.create(name="Sale of Palm Beach Mansion",
    place=palm_beach_mansion,
    timestamp=datetime(2008, 7, 15, 0, 0, 0),
    actors=[
        donald_trump,
        dmitry_rybolovlev,
    ])
