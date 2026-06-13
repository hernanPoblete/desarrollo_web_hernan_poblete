from flask import Blueprint
from utils.db import *
from utils.validation import validate_numeric_str, calc_dv

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


@api.route('user_by_id/<string:id>')
def user_by_id(id):
    parsed_id=id.replace('.', '').replace('-', '')

    if not validate_numeric_str(parsed_id):
        return [""]

    numeric_id = int(parsed_id[:-1])
    dv = int(parsed_id[-1])

    if dv != calc_dv(numeric_id):
        return [""]

    r = db.session.query(miembro).where(miembro.c.id == numeric_id).all()

    if len(r) == 0:
        return [""]


    return [r[0][1]]