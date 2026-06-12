from flask import Blueprint, request, render_template, redirect, make_response
from utils.db import db, comuna, region, miembro
from datetime import datetime
from .validators import validate_member, ValidationError

register_bp = Blueprint('register', __name__, url_prefix='/register')

def register_member(data):
	id = data.get('rut').replace('.', '').replace('-', '')[0:-1]

	
	db.session.execute(
		miembro.insert().values(
			nombre=data.get('nombre'),
			id=id,
			email=data.get('correo'),
			telefono=data.get('telefono'),
			comuna_id=data.get('comuna'),
			fecha_registro=datetime.now()
		)
	)

	db.session.commit()
	


@register_bp.route('/member', methods = ["GET", "POST"])
def register_member_route():

	qreg = db.session.query(region).all()
	if request.method == "GET":
		return render_template("register.html", regiones = qreg)
	elif request.method == "POST":
		try:
			validate_member(request.form)
			register_member(request.form)

			return redirect("/members")
		except ValidationError as e:
			return make_response(render_template("register.html", regiones = qreg, error_msg=e.reason), e.status)

		
		return redirect('/members')



@register_bp.route("/activity", methods = ["GET", "POST"])
def register_activity_route():

	return "OK"
