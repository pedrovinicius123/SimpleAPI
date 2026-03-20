from app.models.message import Message
from controllers.ai_controller import chat
from flask import Response

def get_messages(current_user_id, current_session_id):
    messages = Message.query.filter_by(user_id=current_user_id, session_id=current_session_id).first
    return {'messages': [m.to_dict() for m in messages]}

def add_message(current_user_id, current_session_id, message, db):
    if not message.get('content', False):
        return {"Error": "'Messages' field is mandatory"}, 400
    
    new_message = Message()
    new_message.session_id = current_session_id
    new_message.user_id = current_user_id
    new_message.content = message.get("content")
    db.session.add(new_message)
    db.session.commit()

    return new_message.to_dict(), 200

def edit_message(current_user_id, current_session_id, message_id, new_message, db):
    if not new_message.get("content", False):
        return {"error": "message content must be provided"}, 403
    
    msg = Message.query.filter_by(id=message_id).first()
    msg.content = new_message.get("content")
    db.session.commit()

    def chat_generator():
        for chunk in chat(msg.content):
            yield chunk.message.content

    return Response(chat_generator, 200, mimetype="text/plain")
