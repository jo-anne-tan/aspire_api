from datetime import datetime
from flask import Blueprint, request, jsonify, make_response
from models.tutor_session import Tutor_session
from models.tutor import Tutor
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from playhouse.shortcuts import model_to_dict


tutor_sessions_api_blueprint = Blueprint(
    "tutor_sessions_api", __name__, template_folder="templates")

@tutor_sessions_api_blueprint.route('/new', methods=['POST'])
@jwt_required
def new():
    params = request.json
    tutor_id = get_jwt_identity()
    tutor = Tutor.get_by_id(tutor_id)


    try:
        new_tutor_session = Tutor_session(
            subject = params.get('subject'),
            tutor_id = tutor.id,
            title = params.get('title'),
            price = params.get('price'),
            description = params.get('description'),
            start_time =
            (
                    datetime(
                        int(params.get('start_year')),
                        int(params.get('start_month')),
                        int(params.get('start_day')),
                        int(params.get('start_hour')),
                        int(params.get('start_minute'))
                    )
            ),
            end_time =
            (
                    datetime(
                        int(params.get('end_year')),
                        int(params.get('end_month')),
                        int(params.get('end_day')),
                        int(params.get('end_hour')),
                        int(params.get('end_minute'))
                    )
            ),
            max_student_capacity = params.get('max_student_capacity'),
            status ="Confirmed",
            status_timestamp = datetime.now(),
            zoom_host = "",
            zoom_participant = ""
        )
    except:
        responseObject = {
            "status": "failed",
            "message": ['All fields are required!']
        }
        return make_response(jsonify(responseObject)), 400

    if new_tutor_session.save():
        responseObject = ({
            "message": "Successfully created new tutor session.",
            "status": "success!",
            "session": {
                "id": new_tutor_session.id,
                "title": new_tutor_session.title,
                "description": new_tutor_session.description,
                "subject": new_tutor_session.subject_id,
                "tutor_id" : new_tutor_session.tutor.id,
                "start_time" : new_tutor_session.start_time,
                "end_time" : new_tutor_session.end_time,
                "max_student_capacity" : new_tutor_session.max_student_capacity,
                "price": new_tutor_session.price,
                "status" : new_tutor_session.status,
                "status_timestamp" :new_tutor_session.status_timestamp,
                "zoom_host": new_tutor_session.zoom_host,
                "zoom_participant": new_tutor_session.zoom_participant
            }
        })
        return make_response(jsonify(responseObject)), 201
    else:
        return make_response(jsonify([err for err in new_tutor_session.errors])), 400


@tutor_sessions_api_blueprint.route('/<id>/delete', methods=['POST'])
@jwt_required
def delete(id):
    tutor_session = Tutor_session.get_by_id(id)
    tutor = Tutor.get_by_id(get_jwt_identity())

    if tutor_session:
        if tutor_session.tutor_id == tutor.id:
            if tutor_session.delete_instance():
                responseObject = ({
                    "message": "Successfully deleted tutor session.",
                    "status" : "success!"
                })
                return make_response(jsonify(responseObject)), 200
            else:
                responseObject = {
                    "status": "failed",
                    "message": "Deleting tutor session failed."
                }
                return make_response(jsonify(responseObject)), 400
        else:
            responseObject = ({
                "message": "No permission to delete tutor session.",
                "status" : "failed!"
            })
            return make_response(jsonify(responseObject)), 403
    else:
        responseObject = ({
            "message": "Tutor session does not exist.",
            "status" : "failed!"
        })
        return make_response(jsonify(responseObject)), 500

# @tutor_sessions_api_blueprint.route('/<id>/update', methods=['POST'])
# @jwt_required
# def update(id):
#     tutor_session = Tutor_session.get_by_id(id)
#     tutor = Tutor.get_by_id(get_jwt_identity())


@tutor_sessions_api_blueprint.route('/', methods=['GET'])
def show_all():
    tutor_sessions = Tutor_session.select()

    tutor_sessions_data = []

    for tutor_session in tutor_sessions:
        tutor_session = model_to_dict(tutor_session)
        tutor_sessions_data.append(tutor_session)

    return make_response(jsonify(tutor_sessions_data)), 200

@tutor_sessions_api_blueprint.route('/<id>', methods=['GET'])
def show(id):
    tutor_session = Tutor_session.get_by_id(id)
    tutor_session_data = model_to_dict(tutor_session)

    return make_response(jsonify(tutor_session_data)), 200

@tutor_sessions_api_blueprint.route('/me', methods=['GET'])
@jwt_required
def show_me():
    tutor = Tutor.get_by_id(get_jwt_identity())

    if tutor:
        my_tutor_sessions = Tutor_session.select().where(Tutor_session.tutor_id == tutor.id)

        my_tutor_sessions_data = []

        for tutor_session in my_tutor_sessions:
            tutor_session = model_to_dict(tutor_session)
            my_tutor_sessions_data.append(tutor_session)

        return make_response(jsonify(my_tutor_sessions_data)), 200

@tutor_sessions_api_blueprint.route('/tutor/<id>', methods=['GET'])
def show_tutor_tutorsesions(id):
    tutor = Tutor.get_by_id(id)

    if tutor:
        tutor_sessions = Tutor_session.select().where(Tutor_session.tutor_id == tutor.id)

        tutor_sessions_data = []

        for tutor_session in tutor_sessions:
            tutor_session = model_to_dict(tutor_session)
            tutor_sessions_data.append(tutor_session)

        return make_response(jsonify(tutor_sessions_data)), 200
    else:
        objectResponse = ({
            "message" : "Tutor does not exist.",
            "status" : "erroe!"
        })
        return make_response(jsonify(objectResponse)), 404

