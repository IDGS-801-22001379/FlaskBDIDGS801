from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, Length, NumberRange, Email

class UserForm2(FlaskForm):
    id = IntegerField('ID', [
        NumberRange(min=1, max=20, message='Valor no válido')
    ])
    
    nombre = StringField('Nombre', [
        DataRequired(message='El nombre es requerido'),
        Length(min=4, max=20, message='Requiere min=4 max=20')
    ])
    
    apaterno = StringField('Apellido Paterno', [
        DataRequired(message='El apellido paterno es requerido')
    ])
    
    email = StringField('Correo Electrónico', [
        DataRequired(message='El correo es requerido'),
        Email(message='Ingrese un correo válido')
    ])
