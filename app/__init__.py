# -*- coding: utf-8 -*-
__author__ = 'Rand01ph'

from flask import Flask
from flask.ext.login import LoginManager
from flask.ext.sqlalchemy import SQLAlchemy
from config import config


db = SQLAlchemy()

login_manager = LoginManager()
login_manager.session_protection = 'basic'
login_manager.login_view = 'admin.login'


def create_app(config_name):
	app = Flask(__name__)
	app.config.from_object(config[config_name])
	config[config_name].init_app(app)

	db.init_app(app)
	login_manager.init_app(app)

	from .admin import admin as admin_blueprint
	from .main import main as main_blueprint

	app.register_blueprint(main_blueprint)
	app.register_blueprint(admin_blueprint, url_prefix='/admin')

	return app