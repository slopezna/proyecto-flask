import os, hashlib
from flask_script import Manager
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import Form
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

#clave secreta encriptacion forms
app.config['SECRET_KEY'] = 'tamadre'

#definicion de las clases modelo
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(64), nullable=False, unique=True, index=True)
    cargo = db.Column(db.String(64), nullable=False)
    telefono = db.Column(db.Integer, unique=True, index=True)
    password = db.Column(db.String(256), nullable=False, unique=True)
    correos = db.relationship('Correo', backref='usuario', lazy=True)

class Correo(db.Model):
    id = id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    email = db.Column(db.String(256), unique=True, index=True)

@app.route('/')
def index():
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
    app.run(debug=True, port=80)
