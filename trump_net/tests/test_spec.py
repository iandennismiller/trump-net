# -*- coding: utf-8 -*-
# trump-net (c) Ian Dennis Miller

from nose.plugins.attrib import attr
from .mixins import DiamondTestCase
import situation
import situation.io


class SpecTestCase(DiamondTestCase):
    "Coverage for Situation Specification."

    def setUp(self):
        super(SpecTestCase, self).setUp()
        from trump_net.spec import init
        init()
        # assert trump_net

    @attr("single")
    def test_spec(self):
        p = situation.Person.find(name="Donald Trump")
        assert p

        g = situation.Group.find(name="Trump Clan")
        assert g

        h = situation.io.dump()
        self.assertEqual(h["persons"][0]["name"], "Donald Trump", "person name match")
        self.assertEqual(h["events"][0]["name"], "Trump Tower Meeting", "event name match")
