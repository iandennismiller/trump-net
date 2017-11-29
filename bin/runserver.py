#!/usr/bin/env python
# -*- coding: utf-8 -*-
# trump-net (c) Ian Dennis Miller

import warnings
from flask.exthook import ExtDeprecationWarning
warnings.simplefilter('ignore', ExtDeprecationWarning)

from trump_net.wsgi import app
app.run(port=app.config['PORT'])
