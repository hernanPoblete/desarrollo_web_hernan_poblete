from flask import Blueprint
from utils.db import *

api = Blueprint('api',__name__, url_prefix='/api')

@api.route('/')
def test():
    return {
        'status': 'ok'
    }


@api.route('cities_by_region/<int:region>')
def cities_by_region(region):

    r = list(map(
        lambda x: {'id': x[0], 'comuna': x[1]},
        db.session.query(comuna)
        .where(comuna.c.region_id==region)
        .order_by(comuna.c.nombre)
        .all()))

    return r
