from ..extensions import db
from datetime import datetime

class Message(db.Model):
    __tablename__='messages'

    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.ForeignKey("sessions.id"))
    user_id = db.Column(db.ForeignKey("users.id"))
    content = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'content': self.content,
            'session_id': self.session_id,
            'author_id': self.user_id,
            'created_at': self.created_at.isoformat()
        }
