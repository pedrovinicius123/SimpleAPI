from flask import Blueprint, jsonify, request, redirect, url_for
from controllers.message_controler import add_message
from ..extensions import db, login_manager

bp_llm_agent = Blueprint("ai", __name__, url_prefix="/chat")



@bp_llm_agent.route("/", methods=["GET", "POST"])
def chat():
    if request.method == "GET":
        return "Chat page", 200
    
    else:
        data = request.json
        add_message(data, db)
        

