from flask import Blueprint, request, jsonify, make_response
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from models.student import Student
from playhouse.shortcuts import model_to_dict

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
        responseObject = ({
            "token": token,
            "message": "Successfully created student and signed in.",
            "status": "success!",
            "student": {
                "id": new_student.id,
                "name": new_student.first_name + " " + new_student.last_name,
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


