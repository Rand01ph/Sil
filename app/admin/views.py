# -*- coding: utf-8 -*-
__author__ = 'Rand01ph'

from flask import render_template, redirect, request, url_for, flash
from flask.ext.login import login_user, logout_user, login_required, current_user
from . import admin
from .. import db
from ..models import Admin
from .forms import LoginForm


'''登陆'''


@admin.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		user = Admin.query.filter_by(username=form.username.data).first()
		if user is not None and user.verify_password(form.password.data):
			login_user(user, form.remember_me.data)
			return redirect(request.args.get('next') or url_for('main.index'))
		flash('Invalid username or password')
	return render_template('admin/login.html', form=form)


'''登出'''


@admin.route('/logout')
@login_required
def logout():
	logout_user()
	flash('You have been logged out.')
	return redirect(url_for('main.index'))


'''写博客'''

'''编辑博客'''

'''删除博客'''

'''添加Tag'''

'''编辑Tag'''