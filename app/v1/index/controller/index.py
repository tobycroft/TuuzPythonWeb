from flask import Blueprint

import tuuz.Ret.ret

Index = Blueprint('index', __name__)


@Index.route('/')
@Index.route('/index')
def index():
    return tuuz.Ret.ret.fail(400, None)
