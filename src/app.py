from flask import Flask, url_for, render_template, request, redirect, jsonify
import pathlib
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
import os
from datetime import datetime
from math import ceil

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

def members_length():
	return db.session.query(miembro).count()

def register_member(data):
	print(data.get('rut'))
	id = data.get('rut').replace('.', '').replace('-', '')


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
	

@app.route("/members/<int:page>", methods=["GET"])
def members(page):
	users_per_page = 10
	pages = ceil(members_length()/users_per_page)

	if(page>pages and members_length!=0):
		return redirect("/members/1")
	
	return render_template("dashboard.html", members = fetch_latest_members(users_per_page, (page-1)*users_per_page), page=page, max_page=pages)


@app.route("/api/user", methods=["GET", "POST"])
def fetch_user():
	return jsonify({
		"foo": "bar"
	})
if __name__ == '__main__':

	

	app.run(port=5000, host="0.0.0.0", debug=True, threaded=True)
