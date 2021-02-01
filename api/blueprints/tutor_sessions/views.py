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
            duration = params.get('duration'),
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
            'status': 'failed',
            'message': ['All fields are required!']
        }
        return make_response(jsonify(responseObject)), 400

    if new_tutor_session.save():
        responseObject = ({
            "message": "Successfully created new tutor session.",
            "status": "success!",
            "session": {
                "id": new_tutor_session.id,
                "title": new_tutor_session.title,
                "subject": new_tutor_session.subject_id,
                "tutor_id" : new_tutor_session.tutor_id.id,
                "duration" : new_tutor_session.duration,
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