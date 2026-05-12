from flask import Flask, url_for, render_template, request



app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
	return render_template("dashboard.html")



@app.route("/register", methods = ["GET", "POST"])
def register():
	if request.method == "GET":
		return render_template("register.html")
	

@app.route("/members", methods=["GET"])
def members():
	return render_template("dashboard.html")

app.run(port=5000, host="0.0.0.0", debug=True, threaded=True)
