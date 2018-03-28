from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user, login_required
from . import auth
from ..models import Usuario
from .forms import LoginForm


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if request.method == 'POST':
        usuario = Usuario.query.filter_by(nombre=form.usuario.data).first()
        if usuario is not None and usuario.verify_password(form.password.data):
            print('correcto')
            login_user(usuario)
            return redirect(url_for('main.dashboard'))
        else:
            print('malo')

    return render_template('auth/login.html', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
