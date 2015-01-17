# -*- coding: utf-8 -*-
__author__ = 'Rand01ph'
from flask import Blueprint

main = Blueprint('main', __name__)

from . import views