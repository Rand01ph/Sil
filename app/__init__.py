# -*- coding: utf-8 -*-
__author__ = 'Rand01ph'

from flask import Flask
from flask.ext.login import LoginManager
from flask.ext.sqlalchemy import SQLAlchemy


db = SQLAlchemy()

login_manager = LoginManager()
login_manager.session_protection = 'basic'
login_manager.login_view = 'admin.login'


def create_app():
	app = Flask(__name__)

	db.init_app(app)
	login_manager.init_app(app)

	from .admin import admin as admin_blueprint

	app.register_blueprint(admin_blueprint, url_prefix='/admin')

	return app