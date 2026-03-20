from app.models.message import Message

def get_messages(current_user_id, current_session_id):
    messages = Message.query.filter_by(user_id=current_user_id, session_id=current_session_id)
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
