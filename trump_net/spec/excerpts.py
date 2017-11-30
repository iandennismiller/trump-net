# -*- coding: utf-8 -*-
# trump-net (c) Ian Dennis Miller

from situation import Excerpt, Resource
from .persons import *

Excerpt.create(
    content="Russians make up a pretty disproportionate cross-section of a lot of our assets. " +
    "We see a lot of money pouring in from Russia",
    resource=Resource.find(name="Donald Trump's Many, Many, Many, Many Ties to Russia")
)
