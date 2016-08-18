from app import app, db, lm
from flask import render_template, flash, redirect, session, url_for, request, g
from flask_security import login_user, logout_user, current_user, login_required
from .models import User
from .forms import RegistrationForm, LoginForm


@lm.user_loader
def load_user(user_id):
    return User.get(user_id)


@app.route('/')
def home():
    return "hey there"


@app.route('/register', methods=['POST', 'GET'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(form.email.data, form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Thanks for registering')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('/login.html')
    email = request.form['email']
    password = request.form['password']
    registered_user = User.query.filter_by(email=email, password=password).first()
    if registered_user is None:
        flash('Username or Password is invalid', 'error')
        return redirect(url_for('login'))
    login_user(registered_user)
    flash('Logged in successfully')
    return redirect(url_for('index'))


@app.route('/index/')
@login_required
def index():
    return render_template('index.html')
