# -*- coding: utf-8 -*-
# trump-net (c) Ian Dennis Miller


def init():
    from . import persons
    from . import groups
    from . import events
    from . import resources
    from . import excerpts
    from . import places

    assert persons
    assert groups
    assert events
    assert resources
    assert excerpts
    assert places
