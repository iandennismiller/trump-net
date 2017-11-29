#!/usr/bin/env python
# -*- coding: utf-8 -*-
# trump-net (c) Ian Dennis Miller

import situation

import sys
sys.path.insert(0, '.')

from trump_net import create_app
app = create_app()

with app.app_context():
    import trump_net.spec.persons
    p = situation.Person.find(name="Rob")
    print(p)
    assert p
