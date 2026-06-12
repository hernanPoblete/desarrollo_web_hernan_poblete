from flask import Flask, url_for, render_template, request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
from datetime import datetime
from math import ceil

from utils.db import __prepare_db__
from inject_dotenv import __inject_dotenv__

app = Flask(__name__)

__inject_dotenv__()
__prepare_db__(app)

from utils.db import miembro, db
def fetch_latest_members(n, offset=0):
	return db.session.query(miembro).order_by('fecha_registro').offset(offset).limit(n)

def members_length():
	return db.session.query(miembro).count()



from routes.register.register import register_bp
from routes.api.api import api as api_bp


app.register_blueprint(register_bp)
app.register_blueprint(api_bp)

if bool(os.environ["TEST"]):
	from routes.dev import test_BP
	app.register_blueprint(test_BP, url_prefix="/dev")

@app.route("/", methods=["GET"])
def index():
	return render_template("index.html", members= fetch_latest_members(5))

	

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
