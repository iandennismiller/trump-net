# trump-net (c) Ian Dennis Miller

SHELL=/bin/bash
PROJECT_NAME=trump-net
MOD_NAME=trump_net
WATCHMEDO_PATH=$$(which watchmedo)
NOSETESTS_PATH=$$(which nosetests)
TEST_CMD=SETTINGS=$$PWD/etc/conf/testing.conf $(NOSETESTS_PATH) $(MOD_NAME)

install:
	python setup.py install

spec:
	SETTINGS=$$PWD/etc/conf/dev.conf bin/manage.py spec

requirements:
	pip install -r requirements.txt

develop:
	pip install -r .requirements-dev.txt

clean:
	rm -rf build dist *.egg-info
	find . -name '*.pyc' -delete
	find . -name __pycache__ -delete

server:
	SETTINGS=$$PWD/etc/conf/dev.conf bin/manage.py runserver

server-win:
	set SETTINGS=%cd%\etc\conf\dev-win.conf
	%VIRTUAL_ENV%\scripts\python.exe bin\manage.py runserver

shell:
	SETTINGS=$$PWD/etc/conf/dev.conf bin/manage.py shell

watch:
	watchmedo shell-command -R -p "*.py" -c 'echo \\n\\n\\n\\nSTART; date; $(TEST_CMD) -c etc/nose/test-single.cfg; date' .

test:
	$(TEST_CMD) -c etc/nose/test.cfg

single:
	$(TEST_CMD) -c etc/nose/test-single.cfg

db:
	SETTINGS=$$PWD/etc/conf/dev.conf bin/manage.py init_db
	SETTINGS=$$PWD/etc/conf/dev.conf bin/manage.py user_add --email "guest@example.com" --password "guest"
	SETTINGS=$$PWD/etc/conf/dev.conf bin/manage.py user_add --email "admin@example.com" --password "hzz" --admin

db-win:
	set SETTINGS=%cd%\etc\conf\dev-win.conf
	bin/manage.py init_db
	bin/manage.py user_add --email "guest@example.com" --password "guest"
	bin/manage.py user_add --email "admin@example.com" --password "hzz" --admin

newmigration:
	SETTINGS=$$PWD/etc/conf/dev.conf bin/manage.py drop_db
	SETTINGS=$$PWD/etc/conf/dev.conf bin/manage.py db upgrade
	SETTINGS=$$PWD/etc/conf/dev.conf bin/manage.py db migrate

migrate:
	SETTINGS=$$PWD/etc/conf/dev.conf bin/manage.py db upgrade

apidocs:
	rm -rf var/sphinx/auto-api
	mkdir -p var/sphinx/auto-api/$(MOD_NAME)
	sphinx-apidoc --separate -o var/sphinx/auto-api/$(MOD_NAME) $(MOD_NAME) $(MOD_NAME)/tests
	-rm docs/auto-api
	ln -s $$PWD/var/sphinx/auto-api docs/auto-api

docs:
	rm -rf build/sphinx
	SETTINGS=$$PWD/etc/conf/testing.conf sphinx-build -b html docs build/sphinx

notebook:
	SETTINGS=$$PWD/etc/conf/dev.conf cd var/ipython && ipython notebook

release:
	python setup.py sdist upload

.PHONY: clean install test server watch notebook db single docs shell upgradedb migratedb release requirements apidocs gh-pages develop spec
