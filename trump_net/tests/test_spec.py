# -*- coding: utf-8 -*-
# trump-net (c) Ian Dennis Miller

from nose.plugins.attrib import attr
from .mixins import DiamondTestCase
import situation


class SpecTestCase(DiamondTestCase):
    "Coverage for Situation Specification."

    def setUp(self):
        super(SpecTestCase, self).setUp()
        import trump_net.spec.persons
        assert trump_net

    @attr("single")
    def test_create(self):
        "ensure an account can be created"
        p = situation.Person.find(name="Donald Trump")
        assert p

        g = situation.Group.find(name="Trump Clan")
        assert g

        h = situation.dump()
        self.assertEqual(h["persons"][0]["name"], "Donald Trump", "name match")
