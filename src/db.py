import os
from flask_sqlalchemy import SQLAlchemy

db=None
region=None
comuna=None
miembro=None
actividad=None
foto=None

def __prepare_db__(app):
    app.config["SQLALCHEMY_DATABASE_URI"]=os.environ["DB_URI"]

    global db, region, comuna, miembro, actividad, foto
     
    db = SQLAlchemy(app)
    app.app_context().push()

    region=db.Table('region', db.metadata, autoload_with=db.engine)
    comuna=db.Table('comuna', db.metadata, autoload_with=db.engine)
    miembro=db.Table('miembro', db.metadata, autoload_with=db.engine)
    actividad=db.Table('actividad', db.metadata, autoload_with=db.engine)
    foto=db.Table('foto', db.metadata, autoload_with=db.engine)