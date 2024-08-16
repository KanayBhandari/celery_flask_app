from flask import Blueprint, jsonify
from proj.tasks import what, add, mul

user_bp = Blueprint('user_bp', __name__)


@user_bp.route('/ping', methods=['GET'])
def ping():
    what.delay()
    add.delay(3, 3)
    mul.delay(12345678, 987654321)
    return jsonify(msg='pong')