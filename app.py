from flask import Flask, render_template, redirect, request, url_for, flash
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
import forms
from models import db, Alumnos

# Inicializar Flask
app = Flask(__name__)


app.config.from_object(DevelopmentConfig)


csrf = CSRFProtect(app)


db.init_app(app)

@app.route("/", methods=['GET', 'POST'])
@app.route("/index", methods=['GET', 'POST'])
def index():
    form = forms.UserForm2(request.form)  # Corrección en la creación del formulario
    alumnos = Alumnos.query.all()  # Recuperar los alumnos de la BD
    return render_template("index.html", form=form, alumnos=alumnos)  # Corrección en la clave del contexto



@app.route("/detalles", methods=['GET', 'POST'])
def detalles():
    if request.method == 'GET':
        id = request.args.get('id')

      
        print(f"ID recibido: {id}")

        alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()

        if alum1:
            nombre = alum1.nombre
            apaterno = alum1.apaterno
            email = alum1.email
        else:
            nombre = "No encontrado"
            apaterno = "No encontrado"
            email = "No disponible"

    return render_template("detalles.html", id=id, nombre=nombre, apaterno=apaterno, email=email)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  
    app.run(debug=True)

