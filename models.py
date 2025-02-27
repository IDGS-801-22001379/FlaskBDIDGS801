from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class Alumnos(db.Model):
    __tablename__ = 'alumnos'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    apaterno = db.Column(db.String(100), nullable=False)
    ematerno = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    created_date = db.Column(db.DateTime, default=datetime.datetime.now)

    def __init__(self, nombre, apaterno, ematerno, email):
        self.nombre = nombre
        self.apaterno = apaterno
        self.ematerno = ematerno
        self.email = email
