from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import Required

app = Flask(__name__)
app.config['SECRET_KEY'] = 'tamadre'
Bootstrap(app)

class LoginForm(Form):
    username = StringField('Usuario',validators=[Required()])
    password = PasswordField('Password')
    submit = SubmitField('submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    return render_template('index.html', form=form)

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.route('/config')
def config():
    return render_template('configuracion.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True, port=80)
