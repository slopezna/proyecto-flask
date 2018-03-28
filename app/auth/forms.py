from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Length, Email

class LoginForm(FlaskForm):
    usuario = StringField('Usuario', validators=[Required()])
    password = PasswordField('Contraseña', validators=[Required()])
    submit = SubmitField('Submit')
