from flask import Blueprint, request, make_response
from routes.register.validators import validate_member, ValidationError

test_BP = Blueprint('test', __name__)

@test_BP.route("/")
def test_route():
    return {
        "status": "ok",
        "info": "La ruta de desarrollo/testeo está habilitada"
    }

@test_BP.route("/validateMember", methods=["POST"])
def memberRegisterValidation():
    try:
        validate_member(request.form)
        return {"status": "ok"}
    except ValidationError as e:
        response = make_response({
            "info": e.args[0]
        }, e.status)

        return response