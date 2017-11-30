# -*- coding: utf-8 -*-
# trump-net (c) Ian Dennis Miller

from situation import Place, Person
from .persons import *

"""
Place.create(name="",
    owners=[
    ])
"""

trump_tower = Place.create(name="Trump Tower",
    owners=[
        donald_trump,
    ])

palm_beach_mansion = Place.create(name="Palm Beach Mansion",
    address="515 N. County Rd., Palm Beach, Florida",
    owners=[
        donald_trump,
        dmitry_rybolovlev,
        Person.create(name="Abraham Gosman")
    ])

mar_a_lago = Place.create(name="Mar a Lago",
    owners=[
        donald_trump,
    ])
