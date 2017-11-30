# -*- coding: utf-8 -*-
# trump-net (c) Ian Dennis Miller

from situation import Group
from .persons import *

Group.create(name="Trump Clan",
    members=[
        donald_trump,
        donald_trump_jr,
        fred_trump,
        fred_trump_jr,
        ivana_trump,
        ivanka_trump,
        eric_trump,
        tiffany_trump,
        barron_trump,
        marla_maples,
        melania_trump,
        jared_kushner,
    ])

Group.create(name="Kushner Clan",
    members=[
        jared_kushner,
        ivanka_trump,
        charles_kushner,
    ])

Group.create(name="Maples Clan",
    members=[
        donald_trump,
        marla_maples,
        tiffany_trump,
    ])

Group.create(name="Knavs Clan",
    members=[
        donald_trump,
        melania_trump,
        barron_trump,
    ])

Group.create(name="Zelníčková Clan",
    members=[
        donald_trump,
        donald_trump_jr,
        ivana_trump,
        ivanka_trump,
        eric_trump,
    ])

Group.create(name="Trump Campaign",
    members=[
        donald_trump,
        jared_kushner,
        paul_manafort,
        steve_bannon,
        roger_stone,
        kelly_anne_conway,
    ])

Group.create(name="Trump Administration",
    members=[
        donald_trump,
        jared_kushner,
        steve_bannon,
        kelly_anne_conway,
    ])

Group.create(name="Cambridge Analytica",
    members=[
        steve_bannon,
        robert_mercer,
    ])

Group.create(name="Breitbart",
    members=[
        steve_bannon,
        robert_mercer,
        milo_yiannopoulos,
    ])
