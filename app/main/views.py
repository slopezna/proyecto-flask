from flask import render_template, session, redirect, url_for, current_app
from .. import db
from ..models import Usuario
from ..email import send_email
from . import main
from .forms import LogForm


@main.route('/', methods=['GET', 'POST'])
def index():
    #cambiar entre ok, risk y danger para ver los cambios en el dashboard
    status = 'ok'
    form = LogForm()
    return render_template('home.html', status=status, form=form)

@main.route('/dashboard')
def dashboard():
    #cambiar entre ok, risk y danger para ver los cambios en el dashboard
    status = 'ok'
    return render_template('dashboard.html', status=status)

@main.route('/maquina')
def maquina():
    return render_template('maquina.html')

@main.route('/config')
def config():
    return render_template('config.html')
