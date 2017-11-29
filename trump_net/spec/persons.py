# -*- coding: utf-8 -*-
# trump-net (c) Ian Dennis Miller

# from datetime import datetime
from situation import Person, Group


g = Group.create(name="Trump Clan")
g.members.extend([
    Person.find_or_create(name="Donald Trump"),
    Person.find_or_create(name="Donald Trump, Jr."),
    Person.find_or_create(name="Fred Trump"),
    Person.find_or_create(name="Fred Trump, Jr."),
    Person.find_or_create(name="Ivana Trump"),
    Person.find_or_create(name="Ivanka Trump"),
    Person.find_or_create(name="Eric Trump"),
    Person.find_or_create(name="Tiffany Trump"),
    Person.find_or_create(name="Barron Trump"),
    Person.find_or_create(name="Marla Maples"),
    Person.find_or_create(name="Melania Trump"),
    Person.find_or_create(name="Jared Kushner"),
])

g = Group.create(name="Kushner Clan")
g.members.extend([
    Person.find_or_create(name="Jared Kushner"),
    Person.find_or_create(name="Ivanka Trump"),
    Person.find_or_create(name="Charles Kushner"),
])

g = Group.create(name="Marples Clan")
g.members.extend([
    Person.find_or_create(name="Donald Trump"),
    Person.find_or_create(name="Marla Maples"),
    Person.find_or_create(name="Tiffany Trump"),
])

g = Group.create(name="Knavs Clan")
g.members.extend([
    Person.find_or_create(name="Donald Trump"),
    Person.find_or_create(name="Melania Trump"),
    Person.find_or_create(name="Barron Trump"),
])

g = Group.create(name="Zelníčková Clan")
g.members.extend([
    Person.find_or_create(name="Donald Trump"),
    Person.find_or_create(name="Ivana Trump"),
    Person.find_or_create(name="Ivanka Trump"),
    Person.find_or_create(name="Donald Trump, Jr."),
    Person.find_or_create(name="Eric Trump"),
])

g = Group.create(name="Trump Campaign")
g.members.extend([
    Person.find_or_create(name="Donald Trump"),
    Person.find_or_create(name="Jared Kushner"),
    Person.find_or_create(name="Paul Manafort"),
    Person.find_or_create(name="Steve Bannon"),
])

g = Group.create(name="Trump Administration")
g.members.extend([
    Person.find_or_create(name="Donald Trump"),
    Person.find_or_create(name="Jared Kushner"),
    Person.find_or_create(name="Steve Bannon"),
])
