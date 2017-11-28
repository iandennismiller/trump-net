#!/usr/bin/bash
# trump_net (c) Ian Dennis Miller

source /usr/local/bin/virtualenvwrapper.sh
mkvirtualenv -a . -r requirements-dev.txt trump_net
source ~/.virtualenvs/trump_net/bin/activate
