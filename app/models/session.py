from extensions import db

class Session(db.Model):
    __tablename__="sessions"
    id = db.Column(db.Integer, primary_key=True)
