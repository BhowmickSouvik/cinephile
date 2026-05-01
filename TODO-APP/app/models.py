from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(150), nullable = False, unique = True)
    password = db.Column(db.String(200), nullable = False)
    tasks = db.relationship('Task', backref='user', cascade="all, delete-orphan")


class Task(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    status = db.Column(db.String(20), default = "Pending")
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
