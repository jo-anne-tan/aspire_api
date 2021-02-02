from models.student import Student
from models.tutor_session import Tutor_session
from models.student_tutor_session import Student_tutor_session
from flask import Blueprint, render_template,flash



student_tutor_sessions_blueprint = Blueprint('student_tutor_sessions',
                            __name__,
                            template_folder='templates')

@student_tutor_sessions_blueprint.route('/create')
def create():
    student = Student.get_by_id(2)
    tutor_session=Tutor_session.get_by_id(7)

    new_participant = Student_tutor_session(
        student=student,
        tutor_session=tutor_session,
        zoom_host="some zoom link",
        zoom_participant="some zoom link"
    )

    if new_participant.save():
        flash("successfully saved")
    else:
        flash("not saved")
    return render_template('home.html',errors=new_participant.errors)