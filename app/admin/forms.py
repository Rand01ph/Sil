# -*- coding: utf-8 -*-
__author__ = 'Rand01ph'

from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Length
from wtforms import ValidationError
from ..models import Admin


class LoginForm(Form):
	username = StringField('Username', validators=[Required()])
	password = PasswordField('Password', validators=[Required()])
	remember_me = BooleanField('Keep me logged in')
	submit = SubmitField('Log In')