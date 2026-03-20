from flask import Blueprint, jsonify, request
from ..extensions import db
from app.controllers.message_controler import get_messages, add_message

bp_message = Blueprint("messages", __name__, url_prefix="/messages")

@bp_message.route("/", methods=["POST", "GET"])
def message():
    if request.method == "GET":
        return jsonify(get_messages())    
    else:
        data = request.json
        return jsonify(add_message(data, db))
