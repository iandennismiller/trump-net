# -*- coding: utf-8 -*-
# trump-net (c) Ian Dennis Miller

from ..models import Role, User


def typical_workflow():
    "create some example objects"

    Role.add_default_roles()

    User.register(
        email="guest@example.com",
        password="guest",
        roles=["User"],
    )

    User.register(
        email="admin@example.com",
        password="hzz",
        roles=["Admin"],
    )
