from flask import Flask, url_for, render_template



app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
	return render_template("dashboard_temp.html")


app.run(port=5000, host="0.0.0.0", debug=True, threaded=True)
