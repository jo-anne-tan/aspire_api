from datetime import datetime
from flask import Blueprint, request, jsonify, make_response
from models.tutor_session import Tutor_session
from models.student_tutor_session import Student_tutor_session
from models.tutor import Tutor
from models.student import Student
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from playhouse.shortcuts import model_to_dict


student_tutor_sessions_api_blueprint = Blueprint(
    "student_tutor_sessions_api", __name__, template_folder="templates")

@student_tutor_sessions_api_blueprint.route('/enroll', methods=['POST'])
@jwt_required
def enroll():
    params = request.json
    student = Student.get_by_id(get_jwt_identity())
    tutor_session = Tutor_session.get_by_id(params.get('tutor_session_id'))

    if student:
        new_participant = Student_tutor_session(
            student= student,
            tutor_session = tutor_session,
            zoom_host = "some zoom link",
            zoom_participant = "some zoom link"
        )

    if new_participant.save():
        responseObject = ({
            "message": "Successfully enroll student.",
            "status": "success!",
            "student": {
                "id": new_participant.student.id,
                "name": new_participant.student.first_name + " " + new_participant.student.last_name,
                "age": new_participant.student.age,
                "is_female" : new_participant.student.is_female
            },
            "tutor_session": {
                "id": tutor_session.id,
            }
        })
        return make_response(jsonify(responseObject)), 201
    else:
        return make_response(jsonify([err for err in new_participant.errors])), 400

@student_tutor_sessions_api_blueprint.route('/unenroll', methods=['POST'])
@jwt_required
def unenroll():
    params = request.json
    student = Student.get_by_id(get_jwt_identity())
    tutor_session = Tutor_session.get_by_id(params.get('tutor_session_id'))

    if student:
        student_tutor_session = Student_tutor_session.get(Student_tutor_session.tutor_session_id == tutor_session.id)

    if student_tutor_session.delete_instance():
        responseObject = ({
            "message": "Successfully uneroll tutor session.",
            "status" : "success!"
        })
        return make_response(jsonify(responseObject)), 200

    else:
        responseObject = {
            "status": "failed",
            "message": "Unenroll tutor session failed."
        }
        return make_response(jsonify(responseObject)), 400
