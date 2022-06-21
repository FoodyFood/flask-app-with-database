from flask import Blueprint, render_template, request, redirect, url_for
from . import db
from .models import User
from flask_sqlalchemy import SQLAlchemy

main = Blueprint('main', __name__)

url_prefix="" # For using inside JupyterHub

@main.route('/')
def index():
    return render_template('index.html', url_prefix=url_prefix)


@main.route('/createuser')
def createuser():
    return render_template('createuser.html', result="", url_prefix=url_prefix)


@main.route('/createuser', methods=['POST'])
def createuser_post():
    name = request.form.get('name')
    dob = request.form.get('dob')

    user = User(name=name, dob=dob)
    db.session.add(user)
    db.session.commit()
    return render_template('createuser.html', result="User Created", url_prefix=url_prefix)


@main.route('/deleteuser')
def deleteuser():
    return render_template('deleteuser.html', result="", url_prefix=url_prefix)

@main.route('/deleteconfirm', methods=['POST'])
def deleteconfirm_post():
    userid = request.form.get('userid')
    users = User.query.filter_by(id=userid)
    return render_template('deleteconfirm.html', users=users, url_prefix=url_prefix)

@main.route('/deleteconfirmed', methods=['POST'])
def deleteconfirmed_post():
    userid = request.form.get('userid')
    User.query.filter_by(id=int(userid)).delete()
    db.session.commit()
    return render_template('deleteuser.html', result="User Deleted", url_prefix=url_prefix)


@main.route('/listusers')
def listusers():
    users = User.query.all()
    return render_template('listusers.html', users=users, url_prefix=url_prefix)

