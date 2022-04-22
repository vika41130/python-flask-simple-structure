from flask import Blueprint, request, redirect, jsonify, make_response
import os
from datetime import datetime


user = Blueprint('user', __name__)

@user.route('/user', methods=['GET'])
def get_user():
    _obj = {
        "id": "123",
        "userName": "Edgar Walker"
    }
    response = make_response(jsonify(_obj))
    response.headers["Content-Type"] = "application/json"
    response.status_code = 200
    return response

