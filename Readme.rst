trump-net
=============

Model the Trump Situation

Overview
--------

Flask-Diamond imports many other Flask extensions and glues them all together.  The end result is a model administration view, accounts and high-level account operations (e.g. password reset), testing, documentation, deployment, and more.

Usage
^^^^^

::

    make server
    SETTINGS=$PWD/etc/conf/dev.conf bin/manage.py spec
    SETTINGS=$PWD/etc/conf/dev.conf bin/manage.py user_add -e admin -p hzz -a

Now, open `/tmp/trump.dot` with Graphviz.app

Specification
^^^^^^^^^^^^^

`trump_net/spec` contains all of the specification files related to the situation.

Installation
^^^^^^^^^^^^

The following will install trump-net.

::

    mkdir trump-net
    cd trump-net
    mkvirtualenv -a . trump-net
    make install docs test db server

Documentation
^^^^^^^^^^^^^

http://trump-net.readthedocs.io
