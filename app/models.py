from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import db, login_manager

class Usuario(UserMixin,db.Model):
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

@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))
