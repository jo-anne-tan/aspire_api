from flask import Blueprint, request, jsonify, make_response
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from models.tutor import Tutor
from playhouse.shortcuts import model_to_dict

tutors_api_blueprint = Blueprint('tutor_api',
                             __name__,
                             template_folder='templates')


@tutors_api_blueprint.route('/', methods=['POST'])
def new():
    params = request.json

    try:
        new_tutor = Tutor(first_name=params.get("first_name"), last_name=params.get("last_name"), email=params.get("email"), password=params.get("password"), age=params.get("age"), is_female=params.get("is_female"))
    except:
        responseObject = {
            'status': 'failed',
            'message': ['All fields are required!']
        }
        return make_response(jsonify(responseObject)), 400

    if new_tutor.save():
        token = create_access_token(identity=new_tutor.id)
        responseObject = ({
            "token": token,
            "message": "Successfully created tutor and signed in.",
            "status": "success!",
            "student": {
                "id": new_tutor.id,
                "name": new_tutor.first_name + " " + new_tutor.last_name,
                "age": new_tutor.age,
                "is_female" : new_tutor.is_female
            }
        })
        return make_response(jsonify(responseObject)), 201
    else:
        return jsonify([err for err in new_tutor.errors])

@tutors_api_blueprint.route('/', methods=['GET'])
def show_all():
    tutors = Tutor.select()

    tutor_data = []

    for tutor in tutors:
        tutor = model_to_dict(tutor)
        tutor_data.append(tutor)

    return jsonify(tutor_data), 200

@tutors_api_blueprint.route('/<id>', methods=['GET'])
def show(id):
    tutor = Tutor.get_by_id(id)
    tutor_data = model_to_dict(tutor)

    return jsonify(tutor_data)


