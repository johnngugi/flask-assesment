from app import app, db
from models import User
from flask import render_template, request, redirect, url_for


@app.route('/')
def index():
    myuser = User.query.all()
    return render_template('forms.html', myUser=myuser)


@app.route('/index', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        user = User(request.form['first_name'], request.form['last_name'])
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('index'))
    else:
        return render_template('index.html')


# @app.route('/forms', methods=['POST', 'GET'])
# def forms():
#     return redirect(url_for('index'))

