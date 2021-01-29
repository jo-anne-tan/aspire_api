import json
from models.tutor import Tutor
from models.student import Student
from werkzeug.security import check_password_hash
from flask import Blueprint, jsonify, request, make_response
from flask_jwt_extended import jwt_required, create_access_token


login_api_blueprint = Blueprint(
    "sessions_api", __name__, template_folder="templates")

@login_api_blueprint.route("/student", methods=["POST"])
def student_login():
    params = request.json

    email = params['email']
    password = params['password']

    try:
        user = Student.get_or_none(email=email)

        if user and check_password_hash(user.password, params.get("password")):
            token = create_access_token(identity=user.id)

            responseObject = {
                "token" : token,
                "status": "success!",
                "message": "Succesfully logged in.",
                "email": user.email,
                "id": user.id
            }

            return make_response(jsonify(responseObject)), 200
        else:
            response_object = {
                'status': 'error',
                'message': 'Wrong password or username. Try again.'
            }
            return jsonify(response_object), 404

    except Exception as e:
        print(e)
        response_object = {
            'status': 'error',
            'message': 'Try again.'
        }
        return make_response(jsonify(response_object)), 500


@login_api_blueprint.route("/tutor", methods=["POST"])
def tutor_login():
    params = request.json

    email = params['email']
    password = params['password']

    try:
        user = Tutor.get_or_none(email=email)

        if user and check_password_hash(user.password, password):
            token = create_access_token(identity=user.id)

            responseObject = {
                "token" : token,
                "status": "success!",
                "message": "Succesfully logged in.",
                "email": user.email,
                "id": user.id
            }
            return make_response(jsonify(responseObject)), 200
        else:
            response_object = {
                'status': 'error',
                'message': 'Wrong password or username. Try again.'
            }
            return jsonify(response_object), 404

    except Exception as e:
        print(e)
        response_object = {
            'status': 'error',
            'message': 'Try again.'
        }
        return make_response(jsonify(response_object)), 500
