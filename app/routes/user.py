from flask import Blueprint, jsonify, request
from flask_login import user_logged_in, login_user
from messages import bp_message
from models.user import User
from extensions import login_manager

bp_user = Blueprint("user", __name__, url_prefix="/user")
bp_user.register_blueprint(bp_message)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id)).first()

@bp_user.route("/<username>", methods=["GET", "PUT", "DELETE"])
def user_field(username:str):
    user = User.query.filter_by(username=username).first()
    login_user(user)
    if request.method == "GET":        
        return jsonify(user.to_dict())
    
    elif request.method == "DELETE":


