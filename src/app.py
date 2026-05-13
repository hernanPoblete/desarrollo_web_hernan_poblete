from flask import Flask, url_for, render_template, request, redirect
import pathlib
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
import os
from datetime import datetime


if pathlib.Path('.env').exists:
	load_dotenv('.env')
elif pathlib.Path('.example.env').exists():
	load_dotenv('.example.env')
else:
	raise NameError("Environment variables not found")

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]=os.environ["DB_URI"]

db = SQLAlchemy(app)
app.app_context().push()

region=db.Table('region', db.metadata, autoload_with=db.engine)
comuna=db.Table('comuna', db.metadata, autoload_with=db.engine)
miembro=db.Table('miembro', db.metadata, autoload_with=db.engine)
actividad=db.Table('actividad', db.metadata, autoload_with=db.engine)
foto=db.Table('foto', db.metadata, autoload_with=db.engine)

def fetch_latest_members(n, offset=0):
	return db.session.query(miembro).order_by('fecha_registro').offset(offset).limit(n)

def register_member(data):
	id = data.rut.replace('.', '').replace('-', '')

	db.session.add(
		miembro(
			nombre=data.nombre,
			id=id,
			email=data.correo,
			telefono=data.telefono
		)
	)
	print(data)


@app.route("/", methods=["GET"])
def index():
	return render_template("index.html", members= fetch_latest_members(5))


@app.route("/register", methods = ["GET", "POST"])
def register():
	if request.method == "GET":
		return render_template("register.html", comunas = db.session.query(comuna).all())
	elif request.method == "POST":
		register_member(request.form)
		return redirect('/members')
	

@app.route("/members", methods=["GET"])
def members():
	return render_template("dashboard.html")

if __name__ == '__main__':

	

	app.run(port=5000, host="0.0.0.0", debug=True, threaded=True)
