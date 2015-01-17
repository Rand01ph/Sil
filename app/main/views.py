# -*- coding: utf-8 -*-
__author__ = 'Rand01ph'

from flask import render_template, redirect, request, url_for, flash
from .import main

@main.route('/')
def index():
    return render_template('index.html')