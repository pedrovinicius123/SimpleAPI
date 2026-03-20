from app.extensions import db

class User(db.Model):
    __tablename__= "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True)
    email = db.Column(db.String(255))

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email
        }
    