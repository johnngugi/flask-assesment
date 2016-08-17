from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64), index=True, unique=True)
    last_name = db.Column(db.String(120), index=True, unique=True)

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
