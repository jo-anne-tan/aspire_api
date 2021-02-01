from flask import Blueprint, request, jsonify, make_response
from models.subject import Subject
from playhouse.shortcuts import model_to_dict


subjects_api_blueprint = Blueprint(
    "subjects_api", __name__, template_folder="templates")


@subjects_api_blueprint.route('/', methods=['GET'])
def show_all():
    subjects = Subject.select()

    subject_data = []

    for subject in subjects:
        subject = model_to_dict(subject)
        subject_data.append(subject)

    return make_response(jsonify(subject_data)), 200

@subjects_api_blueprint.route('/<category>', methods=['GET'])
def show(category):
    subject = Subject.get_or_none(category=category)
    subject_data = model_to_dict(subject)

    return make_response(jsonify(subject_data)), 200
