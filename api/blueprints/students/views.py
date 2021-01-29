from flask import Blueprint, request, jsonify, abort
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from models.student import Student
from playhouse.shortcuts import model_to_dict

students_api_blueprint = Blueprint('students_api',
                             __name__,
                             template_folder='templates')


@students_api_blueprint.route('/', methods=['POST'])
def create():
    params = request.json
    new_student = Student(first_name=params.get("first_name"), last_name=params.get("last_name"), email=params.get("email"), password=params.get("password"), age=params.get("age"), is_female=params.get("gender"))
    if new_student.save():
        token = create_access_token(identity=new_student.id)
        return jsonify({
            "token": token,
            "message": "Successfully created student and signed in.",
            "status": "success",
            "student": {
                "id": Student.id,
                "name": Student.first_name + Student.last_name,
                "age": Student.age,
                "is_female" : Student.is_female
            }
        })
    else:
        return jsonify([err for err in new_student.errors])

@students_api_blueprint.route('/', methods=['GET'])
def show():
    students = Student.select()

    student_data = []

    for student in students:
        student = model_to_dict(student)
        student_data.append(student)

    # breakpoint()
    return jsonify(student_data), 200
