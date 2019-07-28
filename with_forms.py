from flask import Flask, request

from threading import Lock
# pip install flask-WTF
from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField
from wtforms.validators import EqualTo


class ContactForm(FlaskForm):
    name = StringField(label='Name', validators=[
        validators.Length(min=4, max=25)
    ])
    email = StringField(label='E-mail', validators=[
        validators.Length(min=6, max=35),
        validators.Email()
    ])
    job = StringField(label='JOB', validators=[
        validators.Length(min=1, max=35),
        validators.Optional()
    ])

class UserForm(ContactForm):
    password = PasswordField('Password', validators=[
        validators.Length(min=6)])
    confirm = PasswordField('Repeat Password', 
        [EqualTo('password', message = 'Passwords must match')])


app = Flask(__name__)
app.config.update(
    DEBUG=True,
    SECRET_KEY='This key must be secret!',
    WTF_CSRF_ENABLED=False
)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        print(request.form)
        form = ContactForm(request.form)
        print(form.validate())

        if form.validate():
            return ('valid', 200)
        else:
            return ('invalid', 400)

    if request.method == 'GET':
        return 'hello world!', 200

@app.route('/form/user', methods=['POST'])
def user():
    r = request.form['name']
    print(r)
    form = UserForm(request.form)
    print(form.validate())

    if form.validate():
        return ('valid', 200)
    else:
        return ('invalid', 400)


if __name__ == '__main__':
    app.run()
