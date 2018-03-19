from flask import Flask, current_app
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER']='smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'martanorambuenavaras'
app.config['MAIL_PASSWORD'] = 'atletico27@'

mail = Mail(app)

@app.route('/')
def index():
    msg = Message('test subject',sender='martanorambuenavaras@gmail.com',recipients=['seblopezn@gmail.com'])
    msg.body = 'text body'
    msg.html = '<b>HTML</b> body'
    mail.send(msg)
    return 'mensaje enviado'

if __name__ == '__main__':
    app.run(debug=True, port=80)
