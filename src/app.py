from flask import Flask, url_for, render_template, request, redirect
import pathlib
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
import os

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

@app.route("/", methods=["GET"])
def index():
	return render_template("index.html")


@app.route("/register", methods = ["GET", "POST"])
def register():
	if request.method == "GET":
		return render_template("register.html")
	elif request.method == "POST":
		return redirect('/members')
	

@app.route("/members", methods=["GET"])
def members():
	return render_template("dashboard.html")

if __name__ == '__main__':

	

	app.run(port=5000, host="0.0.0.0", debug=True, threaded=True)
