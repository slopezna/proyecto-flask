from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import Required

app = Flask(__name__)
app.config['SECRET_KEY'] = 'tamadre'

@app.route('/')
def index():
    #cambiar entre ok, risk y danger para ver los cambios en el dashboard
    status = 'risk'
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
