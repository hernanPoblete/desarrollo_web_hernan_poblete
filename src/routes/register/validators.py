from utils.db import db, comuna, miembro
from utils.validation import calc_dv

class ValidationError(Exception):
    def __init__(self, reason: str, status: int = 400):
        super()
        self.reason = reason
        self.status = status



def validate_member(data):

    if not data.get("rut"):
        raise ValidationError("El RUT es obligatorio")
    
    nombre=data.get('nombre')
    id=data.get('rut').replace('.', '').replace('-', '')[0:-1]

    dv=int(data.get('rut')[-1].replace("k", "10"))

    email=data.get('correo')
    telefono=data.get('telefono')
    comuna_id=data.get('comuna')

    if not nombre:
        raise ValidationError("El nombre es obligatorio")
    if not email:
        raise ValidationError("Una direccion de e-mail es obligatoria")
    if not telefono:
        raise ValidationError("Un numero de telefono es obligatorio")
    if not comuna_id:
        raise ValidationError("Una comuna debe ser provista")
    
    if len(nombre)>255:
        raise ValidationError("El nombre entregado es muy largo")
    if len(telefono)>15:
        raise ValidationError("El numero de telefono es muy largo")
    if len(email)>80:
        raise ValidationError("La direccion de e-mail entregada es muy larga")

    if not (calc_dv(int(id)) == dv):
        raise ValidationError("El rut entregado no es válido")


    users = db.session.query(miembro).where(miembro.c.id == int(id)).all()
    if (users):
        raise ValidationError("El usuario ya se encuentra registrado")

    cid = db.session.query(comuna).where(comuna.c.id == comuna_id).all()
    if not (cid):
        raise ValidationError("La comuna ingresada no es valida")

    