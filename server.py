import os
from werkzeug.security import generate_password_hash, check_password_hash
from flask_script import Manager
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import Required
from flask_sqlalchemy import SQLAlchemy

#directorio base de la aplicacion
directorioBase = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

#configuracion de SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///' + os.path.join(directorioBase, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#objeto SQLAlchemy instanciado
db = SQLAlchemy(app)

#manager para los scripts
manager = Manager(app)

#clave secreta encriptacion forms
app.config['SECRET_KEY'] = 'tamadre'

#definicion de las clases modelo
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(64), nullable=False, unique=True, index=True)
    cargo = db.Column(db.String(64), nullable=False)
    telefono = db.Column(db.Integer, unique=True, index=True)
    password_hash = db.Column(db.String(256), nullable=False, unique=True)
    correos = db.relationship('Correo', backref='usuario', lazy=True)

    @property
    def password(self):
        raise AttributeError('La contraseña no es un atributo legible')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


class Correo(db.Model):
    id = id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    email = db.Column(db.String(256), unique=True, index=True)

#forms
class LogForm(FlaskForm):
    usuario = StringField('Usuario', validators=[Required()])
    password = PasswordField('Contraseña')
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    #cambiar entre ok, risk y danger para ver los cambios en el dashboard
    status = 'ok'
    form = LogForm()
    return render_template('login.html', status=status, form=form)

@app.route('/dashboard')
def dashboard():
    #cambiar entre ok, risk y danger para ver los cambios en el dashboard
    status = 'ok'
    return render_template('index.html', status=status)

@app.route('/maquina')
def maquina():
    return render_template('maquina.html')

@app.route('/config')
def config():
    return render_template('config.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    manager.run()
    #python server.py runserver -p 80
    #app.run(debug=True, port=80)
