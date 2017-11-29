#!/usr/bin/env python
# -*- coding: utf-8 -*-
# trump-net (c) Ian Dennis Miller


from flask_script import Manager, Shell, Server
from flask_migrate import Migrate, MigrateCommand, upgrade
import alembic
import alembic.config
import sys
import warnings
from flask.exthook import ExtDeprecationWarning
warnings.simplefilter('ignore', ExtDeprecationWarning)

sys.path.insert(0, '.')
from trump_net import create_app, db
from trump_net.models import User, Role

app = create_app()
migrate = Migrate(app, db, directory="trump_net/migrations")


def _make_context():
    return {
        "app": app,
        "db": db,
    }

manager = Manager(app)
manager.add_command("shell", Shell(make_context=_make_context))
manager.add_command("runserver", Server(port=app.config['PORT']))
manager.add_command("publicserver", Server(port=app.config['PORT'], host="0.0.0.0"))
manager.add_command('db', MigrateCommand)


@manager.option('-e', '--email', help='email address', required=True)
@manager.option('-p', '--password', help='password', required=True)
@manager.option('-a', '--admin', help='make user an admin user', action='store_true', default=None)
def user_add(email, password, admin=False):
    "add a user to the database"
    if admin:
        roles = ["Admin"]
    else:
        roles = ["User"]
    User.register(
        email=email,
        password=password,
        confirmed=True,
        roles=roles
    )


@manager.option('-e', '--email', help='email address', required=True)
def user_del(email):
    "delete a user from the database"
    obj = User.find(email=email)
    if obj:
        obj.delete()
        print("Deleted")
    else:
        print("User not found")


@manager.command
def drop_db():
    "drop all databases, instantiate schemas"
    db.reflect()
    db.drop_all()


@manager.option('-m', '--migration',
    help='create database from migrations',
    action='store_true', default=None)
def init_db(migration):
    "drop all databases, instantiate schemas"
    db.drop_all()

    if migration:
        # create database using migrations
        print("applying migration")
        upgrade()
    else:
        # create database from model schema directly
        db.create_all()
        db.session.commit()
        cfg = alembic.config.Config("trump_net/migrations/alembic.ini")
        alembic.command.stamp(cfg, "head")
    Role.add_default_roles()


@manager.command
def spec():
    "apply situation specification"
    db.drop_all()
    db.create_all()
    db.session.commit()
    import trump_net.spec.persons
    assert trump_net

if __name__ == "__main__":
    manager.run()
