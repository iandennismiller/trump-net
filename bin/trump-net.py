#!/usr/bin/env python
# -*- coding: utf-8 -*-
# trump-net (c) Ian Dennis Miller

import sys
sys.path.insert(0, '.')
from trump_net import main
from trump_net.debug_app import create_app

app = create_app()
with app.app_context():
    main()
