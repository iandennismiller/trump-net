# -*- coding: utf-8 -*-
# trump-net (c) Ian Dennis Miller

from situation import Resource, Event, Person, Excerpt, Place, Item, Group
assert Resource and Event and Person and Excerpt and Place and Item and Group


def main():
    Person.create(name="Donald Trump")
    Person.create(name="Donald Trump, Jr.")

    for p in Person.query.all():
        print(p.dumps())

if __name__ == '__main__':
    main()
