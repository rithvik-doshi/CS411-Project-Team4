from flask_mongoengine import db

class User(db.Document):
    username = db.StringField(required=True)
    password = db.StringField(required=True)