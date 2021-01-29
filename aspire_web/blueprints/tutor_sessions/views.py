import datetime
from models.tutor import Tutor
from models.subject import Subject
from models.tutor_session import Tutor_session
from flask import Blueprint, flash, render_template,request,redirect,url_for


tutor_sessions_blueprint = Blueprint('tutor_sessions',
                            __name__,
                            template_folder='templates')

@tutor_sessions_blueprint.route('/new', methods=['GET'])
def new():
    return render_template('tutor_sessions/new.html')

@tutor_sessions_blueprint.route('/create')
def create():
    english = Subject.get_by_id(3)
    math = Subject.get_by_id(4)
    life_skills = Subject.get_by_id(5)

    tutor_1 = Tutor.get_by_id(1)
    tutor_2 = Tutor.get_by_id(2)

    start_1 = datetime.datetime(2021,2,1,10,0)
    end_1 = datetime.datetime(2021,2,1,12,0)
    duration_1 = (end_1-start_1).seconds//60 # convert to minute

    start_2=datetime.datetime(2021,2,1,11,0)
    end_2=datetime.datetime(2021,2,1,13,0)
    duration_2 = (end_2 - start_2).seconds//60 # convert to minute

    session = Tutor_session(
        subject = english,
        tutor = tutor_1,
        title = "Some title",
        price=100,
        duration=duration_1,
        start_time=start_1,
        end_time=end_1,
        max_student_capacity=10,
        status="Confirmed",
        zoom_host="",
        zoom_participant=""
    )

    if session.save():
        flash("session created")
    else:
        flash("error creating session")
    return render_template('home.html',errors=session.errors)