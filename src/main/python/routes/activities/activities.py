from flask import Blueprint, redirect, render_template, request


activities_bp = Blueprint('activities',__name__, url_prefix='/activities')


@activities_bp.route('/check')
def activity():
    if 'id' in request.args.keys():
        return render_template("activity.html")
    return redirect("/activities")

@activities_bp.route("/")
def activities():
    return redirect("/")