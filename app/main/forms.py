from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import Required

class LogForm(FlaskForm):
    usuario = StringField('Usuario', validators=[Required()])
    password = PasswordField('Contraseña')
    submit = SubmitField('Submit')
