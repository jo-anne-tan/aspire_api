from flask import Blueprint, flash, render_template,request,redirect,url_for,session,abort
from models.student import Student

students_blueprint = Blueprint('students',
                            __name__,
                            template_folder='templates')


@students_blueprint.route('/create')
def create():

    new_student = Student(
        first_name="John",
        last_name= "Dane",
        age=43,
        is_female= False,
        email='AAA1@gmail.com',
        password='AAA1@gmail.com'
    )

    if new_student.save():
        flash("Student created!")

        # updating username
        username = new_student.first_name+new_student.last_name+str(new_student.id)
        new_student.username=username
        new_student.save()
        
    else:
        flash("Error creating student!")

    return render_template('home.html', errors = new_student.errors)