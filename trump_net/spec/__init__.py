# -*- coding: utf-8 -*-
# trump-net (c) Ian Dennis Miller


def init():
    from . import persons
    from . import groups
    from . import events

    assert persons
    assert groups
    assert events
