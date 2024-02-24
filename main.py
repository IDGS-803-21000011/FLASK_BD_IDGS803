from flask import Flask, render_template, request, flash, Response, g, redirect
from flask_wtf.csrf import CSRFProtect
import forms
from config import DevelopmentConfig
from models import db, Alumnos

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
crsf = CSRFProtect()

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route("/index")
def index():
    escuela = "UTL!!!"
    alumnos = ["Gael", "Pedro", "Alicia", "Ana"]
    return render_template("index.html", escuela = escuela, alumnos = alumnos)

@app.route("/alumnos", methods=["GET", "POST"])
def alumn():
    nom = ''
    apa = ''
    ama = ''
    alum_form = forms.UserForm(request.form)
    if request.method == "POST" and alum_form.validate():
        nom = alum_form.nombre.data
        apa = alum_form.apaterno.data
        ama = alum_form.amaterno.data
        mensaje = "Bienvenido {}".format(nom)
        flash(mensaje)
        print("Nombre: {}".format(nom))
        print("apaterno: {}".format(apa))
        print("amaterno: {}".format(ama))
    return render_template("alumnos.html", form = alum_form, nom=nom, apa=apa, ama=ama)

if __name__ == "__main__":
    crsf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run()