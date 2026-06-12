from flask import Blueprint, request, render_template
from utils.db import db, comuna, region


register_bp = Blueprint('register', __name__, url_prefix='/register')

@register_bp.route('/member', methods = ["GET", "POST"])
def register_member():
	if request.method == "GET":
		return render_template("register.html", comunas = db.session.query(comuna).all(), regiones = db.session.query(region).all())
	elif request.method == "POST":
		register_member(request.form)
		return redirect('/members')


