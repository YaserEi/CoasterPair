from flask import Flask, render_template, request, Response, flash, redirect, url_for
import flask
from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import Users, db , app
import requests


if __name__ == '__main__':
    app.debug = True
    app.run()

app.config.from_object('config')
moment = Moment(app)
db.init_app(app)
with app.app_context():
    db.create_all()



@app.after_request
def after_request(response):
    response.headers.add('Access_Control_Allow_Headers', 'Content-Type, Authorization, True')
    response.headers.add('Access_control_Allow_Methods', "GET, POST, PATCH, DELETE, OPTIONS")

    return response


@app.route('/')
def index():
  return render_template('pages/home.html')


@app.route('/register', methods=['GET'])
def register_form():
  form = register()
  return render_template('pages/register.html', form=form)

@app.route('/register', methods= ['POST'])
def register():
  first_name = request.args.get('fname')
  last_name = request.args.get('lname')
  email = request.args.get('email')
  password = request.args.get('password')
  coaster_id= request.args.get('Coaster ID')


  user = Users(first_name = first_name, last_name = last_name, email = email, password = password, \
    coaster_id = coaster_id)

  db.session.add(user)
  db.session.commit()
  db.session.close()
  return render_template('pages/login.html')


@app.route('/login', methods=['GET'])
def login():
  email = request.args.get('email')
  password = request.args.get('password')


  user = Users.query.filter_by(email = email).first()
  if password == user.password:
    return render_template('pages/pair.html')
  else:
    return render_template('pages/login.html')



@app.route('/pair', methods=['GET'])
def pair():
 coaster_id = request.args.get('coaster_id')
 return render_template('pages/pair.html')

