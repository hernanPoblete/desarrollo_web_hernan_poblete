from flask import Blueprint
from utils.db import *
from utils.validation import validate_numeric_str, calc_dv
from sqlalchemy import text

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

@api.route('members_by_day')
def members_by_day():
    query= db.session.execute(
        text("SELECT fecha_registro,COUNT(*) FROM miembro GROUP BY (miembro.fecha_registro) ORDER BY fecha_registro;")   
    )

    
    return list(map(lambda x: {'date': str(x[0].year) + '-' + str(x[0].month) + '-' + str(x[0].day) , 'count': x[1]}, 
    list(query.fetchall())))


@api.route('activities_per_city')
def activities_per_city():
    query=db.session.execute(
        text("SELECT c.nombre, count(*) FROM actividad JOIN miembro on miembro.id=actividad.miembro_id JOIN comuna c on miembro.comuna_id=c.id group by c.nombre;")
    )

    return list(map(lambda x: {"comuna": x[0], "count": x[1]}, query.fetchall()))

@api.route('activities_per_type')
def activities_per_type():
    query = db.session.execute(
        text("SELECT tipo, COUNT(*) FROM actividad group by actividad.tipo ;")
    )


    return list(map(lambda x: {"tipo": x[0], "count": x[1]}, query.fetchall()))