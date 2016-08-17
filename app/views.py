from app import app, db
from flask import render_template, flash, redirect, session, url_for, request, g
from flask_security import login_user, logout_user, current_user, login_required
from .models import User
from .forms import RegistrationForm, LoginForm


@app.route('/register', methods=['POST', 'GET'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        user = User(form.email.data,
                    form.password.data)
        db.session.add(user)
        flash('Thanks for registering')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.get(form.email.data)
        if user:
            user.authenticated = True
            db.session.add(user)
            db.session.commit()
            login_user(user, remember=True)
            return redirect(url_for('index'))
    return render_template('login.html', form=form)


@app.route('/index')
def index():
        return render_template('index.html')
