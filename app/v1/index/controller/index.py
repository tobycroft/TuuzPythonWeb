from flask import Blueprint

import tuuz.Ret.ret
import tuuz.database.database

Index = Blueprint('index', __name__)


@Index.route('/')
@Index.route('/index')
def index():
    data = tuuz.database.database.Db().table("coin").select()
    return tuuz.Ret.ret.fail(400, data)
