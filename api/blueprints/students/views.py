from app import app
from models.student import Student
from werkzeug.utils import secure_filename
from playhouse.shortcuts import model_to_dict
from api.util.helpers import upload_file_to_s3
from flask import Blueprint, request, jsonify, make_response, abort
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
import time


students_api_blueprint = Blueprint('students_api',
                             __name__,
                             template_folder='templates')


@students_api_blueprint.route('/', methods=['POST'])
def new():
    params = request.json

    try:
        new_student = Student(first_name=params.get("first_name"), last_name=params.get("last_name"), email=params.get("email"), password=params.get("password"), age=params.get("age"), is_female=params.get("is_female"))
    except:
        responseObject = {
            'status': 'failed',
            'message': ['All fields are required!']
        }
        return make_response(jsonify(responseObject)), 400

    if new_student.save():
        token = create_access_token(identity=new_student.id)
        username = new_student.first_name.lower() + new_student.last_name.lower() + str(new_student.id)
        new_student.username = username
        new_student.save(only=[Student.username])
        responseObject = ({
            "token": token,
            "message": "Successfully created student and signed in.",
            "status": "success!",
            "student": {
                "id": new_student.id,
                "name": new_student.first_name + " " + new_student.last_name,
                "username" : new_student.username,
                "age": new_student.age,
                "is_female" : new_student.is_female
            }
        })

        return make_response(jsonify(responseObject)), 201
    else:
        return make_response(jsonify([err for err in new_student.errors])), 400

@students_api_blueprint.route('/', methods=['GET'])
def show_all():
    students = Student.select()

    student_data = []

    for student in students:
        student = model_to_dict(student)
        student_data.append(student)

    return make_response(jsonify(student_data)), 200

@students_api_blueprint.route('/<id>', methods=['GET'])
def show(id):
    student = Student.get_by_id(id)
    student_data = model_to_dict(student)

    return make_response(jsonify(student_data)), 200

@students_api_blueprint.route('/me', methods=['GET'])
@jwt_required
def me():
    student = Student.get_by_id(get_jwt_identity())
    if student:
        student_data = model_to_dict(student)

        return make_response(jsonify(student_data)), 200
    else:
        return abort(404)

@students_api_blueprint.route('/update-profile-picture', methods=['POST'])
@jwt_required
def update_profile_picture():
    student = Student.get_by_id(get_jwt_identity())

    file = request.files['profile_image']
    file.filename = secure_filename(file.filename)
    image_path = upload_file_to_s3(file, "student", student.username)

    student.profile_image = image_path

    if student.save():
        objectResponse = ({
            "message": "Succesfully updated profile image.",
            "status" : "success!",
            "image"  : {
                "url" : f"{app.config.get('S3_LOCATION')}{image_path}"
            }
        })
        time.sleep(100)
        return make_response(jsonify(objectResponse)), 200
    else:
        return make_response(jsonify([err for err in student.errors])), 400


