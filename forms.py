from wtforms import Form
from wtforms import StringField, SelectField, RadioField, EmailField, IntegerField
from wtforms import validators

class UserForm(Form):
    nombre = StringField('nombre', [
        validators.DataRequired(message='El campo es requerido.'),
        validators.length(min=4, max=10, message='Ingresa un nombre válido.')
    ])
    apaterno = StringField('apaterno', [
        validators.DataRequired(message='El campo es requerido.'),
        validators.length(min=4, max=10, message='Ingresa un apellido paterno válido.')
    ])
    amaterno = StringField('amaterno', [
        validators.DataRequired(message='El campo es requerido.'),
        validators.length(min=4, max=10, message='Ingresa un apellido materno válido.')
    ])
    edad = IntegerField('edad', [
        validators.number_range(min=1, max=10, message='Valor no válido.')
    ])
    correo = EmailField('correo', [
        validators.Email(message='Ingrese un correo válido.')
    ])
