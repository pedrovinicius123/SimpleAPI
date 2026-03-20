from app.models.message import Message
from uuid import uuid4

def get_messages():
    messages = Message.query.all()
    return {'messages': [m.to_dict() for m in messages]}

def add_message(message, db):
    if not message.get('content', False):
        return {"Error": "'Messages' field is mandatory"}, 400
    
    new_message = Message()
    new_message.content = message.get("content")
    db.session.add(new_message)
    db.session.commit()

    return new_message.to_dict(), 200
