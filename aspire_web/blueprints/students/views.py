from flask import Blueprint, flash, render_template,request,redirect,url_for,session,abort
from models.student import Student

students_blueprint = Blueprint('students',
                            __name__,
                            template_folder='templates')


@students_blueprint.route('/new', methods=['GET'])
def new():
    return render_template('students/new.html')

@students_blueprint.route('/create', methods=['POST'])
def create():
    # request.form["female"] returns True if select, 
    # else it returns error
    try:
        is_female = request.form["female"]
    except:
        is_female = False

    new_student = Student(
        first_name=request.form["first_name"],
        last_name= request.form["last_name"],
        age=request.form["age"],
        is_female= is_female,
        email=request.form["email"],
        password=request.form["password"]
    )

    if new_student.save():
        flash("Student created!")
        return redirect(url_for('home'))
    else:
        flash("Error creating student!")
        return render_template('home.html', errors = new_student.errors)