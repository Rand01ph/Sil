# -*- coding: utf-8 -*-
__author__ = 'Rand01ph'

from flask import render_template, redirect, request, url_for, flash
from .import main

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/about')
def about():
	return render_template('about.html')

@main.route('/contact')
def contact():
	return render_template('contact.html')
