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

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
