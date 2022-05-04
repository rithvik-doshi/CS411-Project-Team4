from flask_mongoengine import MongoEngine

class User(db.Document):
    username = db.StringField(required=True)
    password = db.StringField(required=True)