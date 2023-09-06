from models import db, User
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf.csrf import CSRFProtect
from forms import RegistrationForm
import hashlib
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)
app.config['SECRET_KEY'] = b'3872f21b8a9e54d11f6dade833bba5f9c4d3e7ccbf63196a7131f184697b566b'
csrf = CSRFProtect(app)


@app.route('/')
def index():
    return redirect(url_for('register'))


@app.cli.command("init-db")
def init_db():
    db.create_all()



@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        # Обработка данных из формы
        name = form.username.data
        surname = form.surname.data
        email = form.email.data
        password = form.password.data
        print(name, surname, email, password)
        salt = os.urandom(32)
        password_protection = password
        key = hashlib.pbkdf2_hmac('sha256', password_protection.encode('utf-8'), salt, 100000, dklen=128)
        user = User(username=name, surname=surname, email=email, password=key)
        print(user)
        db.session.add(user)
        db.session.commit()
        return f'<h2>Пользователь под именем: {name} добавлен в базу !</h2>' \
               f'<h3> Пароль зашифрован !<br> Экземпляр:<br>{user}</h3><br>(пароль - BLOB массив двоичных данных)'
    return render_template('register.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)