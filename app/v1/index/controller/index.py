import os

from flask import Blueprint

Index = Blueprint('index', __name__)


@Index.route('/')
@Index.route('/index')
def index():
    return 'Index'
