from flask import Blueprint, jsonify, request
from ..extensions import db
from app.controllers.message_controler import get_messages, add_message, edit_message
from models.message import Message
from models.user import User

bp_message = Blueprint("messages", __name__, url_prefix="/messages")

@bp_message.route("/", methods=["POST", "GET"])
def message():
    if request.method == "GET":
        return jsonify(get_messages())    
    else:
        data = request.json
        return jsonify(add_message(data, db))
    
@bp_message.route("/<id>", methods=["GET", "PUT", "DELETE"])
def message_id(id:str):
    if request.method == "GET":
        msg = Message.query.filter_by(int(id)).first()
        return jsonify(msg.to_dict())
    
    elif request.method == "PUT":
        edit_message()

