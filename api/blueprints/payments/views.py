from datetime import datetime
from flask import Blueprint, request, jsonify, make_response
from models.student_tutor_session import Student_tutor_session
from models.student import Student
from models.tutor_session import Tutor_session
from models.payment import Payment
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from playhouse.shortcuts import model_to_dict


payments_api_blueprint = Blueprint('payments_api',
                            __name__,
                            template_folder='templates')

@payments_api_blueprint.route('/new', methods=['POST'])
@jwt_required
def new():
    student = Student.get_by_id(get_jwt_identity())
    params = request.json

    if student:
        student_tutor_session = Student_tutor_session.get_by_id(params.get("student_tutor_session"))
        tutor_session =  Tutor_session.get_by_id(student_tutor_session.tutor_session_id)
        # duration = tutor_session.duration
        # amount = tutor_session.price * duration # price per hour * hrs
        amount = tutor_session.price

        new_payment = Payment(
            student_tutor_session_id = student_tutor_session.id,
            amount = amount,
            status = 'complete',
            status_timestamp = datetime.now()
        )

    if new_payment.save():
        responseObject = (
            {
                "message" : "Payment completed." ,
                "status" : "success!",
                "payment" : {
                    "id" : new_payment.id,
                    "amount" : new_payment.amount,
                    "status" : new_payment.status,
                    "status_timestamp" : new_payment.status_timestamp,
                    "student_tutor_session" : new_payment.student_tutor_session_id
                }
            }
        )
        return make_response(jsonify(responseObject)), 201
    else:
        return make_response(jsonify([err for err in new_payment.errors])), 400


@payments_api_blueprint.route('/update', methods=['POST'])
@jwt_required
def update():
    student = Student.get_by_id(get_jwt_identity())
    params = request.json

    if student:
        payment = Payment.get_by_id(params.get("payment_id"))
        payment.status = 'complete'
        payment.status_timestamp = datetime.now()

    if payment.save():
        responseObject = (
            {
                "message" : "Payment received." ,
                "status" : "success!",
                "payment" : {
                    "id" : payment.id,
                    "amount" : payment.amount,
                    "status" : payment.status,
                    "status_timestamp" : payment.status_timestamp,
                    "student_tutor_session" : payment.student_tutor_session_id
                }
            }
        )
        return make_response(jsonify(responseObject)), 200
    else:
        return make_response(jsonify([err for err in payment.errors])), 400