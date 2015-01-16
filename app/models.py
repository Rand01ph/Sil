# -*- coding: utf-8 -*-
__author__ = 'Rand01ph'

from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask.ext.sqlalchemy import BaseQuery
from flask.ext.login import UserMixin
from app import db, login_manager


class Admin(UserMixin, db.Model):
	"""There should ever only be one admin"""

	__tablename__ = 'admin'

	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(), unique=True)
	email = db.Column(db.String(), unique=True)
	password_hash = db.Column(db.String(128))

	def __init__(self, username, email):
		self.username = username
		self.email = email

	@property
	def password(self):
		raise AttributeError('password is not a readable attribute')

	@password.setter
	def password(self, password):
		self.password_hash = generate_password_hash(password)

	def verify_password(self, password):
		return check_password_hash(self.password_hash, password)


@login_manager.user_loader
def load_user(admin_id):
	return Admin.query.get(int(admin_id))