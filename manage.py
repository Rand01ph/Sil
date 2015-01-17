# -*- coding: utf-8 -*-
__author__ = 'Rand01ph'

import os
from app import create_app, db
from app.models import Admin
from flask.ext.script import Manager, Server

app = create_app('default')
manager = Manager(app)

manager.add_command("runserver", Server(use_debugger=True))

if __name__ == '__main__':
	manager.run()