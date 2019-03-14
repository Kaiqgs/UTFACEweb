from app import db

class Contact(db.Model):
    __tablename__ = "contacts"
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(255))
    name = db.Column(db.String(255))
    age = db.Column(db.Integer)
    grade = db.Column(db.String(255)) # Grade (Série da escola)
    message = db.Column(db.String)
    source = db.Column(db.String(255))
