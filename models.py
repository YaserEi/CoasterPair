from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import false


app = Flask(__name__)
db = SQLAlchemy()
migrate = Migrate(app, db)








app = Flask(__name__)
db = SQLAlchemy()
migrate = Migrate(app, db)

class Users(db.Model):
    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)
    coaster_id = db.Column(db.String)
    pair1 = db.Column(db.String)





