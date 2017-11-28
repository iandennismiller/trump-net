# -*- coding: utf-8 -*-
# trump-net (c) Ian Dennis Miller

from nose.plugins.attrib import attr
from flask_testing import TestCase
from flask_diamond import db
from .debug_app import create_app
# from datetime import datetime
from situation import Person


def simple_situation():
    person1 = Person.create(name="Rob")
    assert person1


class BasicTestCase(TestCase):

    def create_app(self):
        return(create_app())

    def setUp(self):
        db.drop_all()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    @attr("single")
    def test_basic(self):
        "ensure the minimum test works"
        simple_situation()
