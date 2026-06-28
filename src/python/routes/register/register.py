from flask import Blueprint, request, render_template, redirect, make_response
from utils.db import db, comuna, region, miembro, actividad, foto
from datetime import datetime
from .validators import validate_member, ValidationError
import os

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
			fecha_registro=datetime.today()
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
		except ValidationError as e:
			return make_response(render_template("register.html", regiones = qreg, error_msg=e.reason), e.status)

		
		return redirect('/register/activity')



@register_bp.route("/activity", methods = ["GET", "POST"])
def register_activity_route():

	if request.method == 'GET':
		return render_template("register_activity.html")

	else:

		q = request.form.get

		stmt = actividad.insert().values(
			nombre=q('nombre'),
			dia=q('horario'),
			tipo=q('tipo_actividad'),
			miembro_id = q('rut').replace('.', '').replace('-', '')[0:-1],
			duracion = q('duracion'),
			descripcion=q('descripcion'),
			hora_inicio = q("horaInicio")
		)


		result = db.session.execute(stmt)

		folder = result.inserted_primary_key[0]
		nombre_carpeta = 'src/static/uploads/'+str(folder)
		os.makedirs(nombre_carpeta, exist_ok=True)

		for file in request.files.getlist('fotos'):
			ruta = nombre_carpeta+'/'+file.filename
			file.save(ruta)

			foto.insert().values(
				ruta_archivo = ruta,
				nombe_archivo=file.filename,
				actividad_id=folder
			)


		db.session.commit()

		

		return redirect('/?s_msg="Actividad Creada con éxito"')
