from flask import Blueprint, render_template,flash
from models.student_tutor_session import Student_tutor_session
from models.tutor_session import Tutor_session
from models.payment import Payment

payments_blueprint = Blueprint('payments',
                            __name__,
                            template_folder='templates')

@payments_blueprint.route('/create')
def create():
    student_tutor_session = Student_tutor_session.get_by_id(1)
    tutor_session =  Tutor_session.get_by_id(student_tutor_session.tutor_session)
    duration = tutor_session.duration 
    amount = tutor_session.price*duration/60 # hourly rate * hrs

    print(f"the amount is {amount}")

    new_payment = Payment(
        student_tutor_session=student_tutor_session,
        amount=amount,
    )

    if new_payment.save():
        flash("transaction saved")
    else:
        flash("transaction failed")
    return render_template('home.html', errors = new_payment.errors)