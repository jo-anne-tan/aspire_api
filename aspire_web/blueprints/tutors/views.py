from flask import Blueprint, flash, render_template,request,redirect,url_for,session,abort

tutors_blueprint = Blueprint('tutors',
                            __name__,
                            template_folder='templates')

@tutors_blueprint.route('/new', methods=['GET'])
def new():
    return render_template('tutors/new.html')

@tutors_blueprint.route('/create', methods=['POST'])
def create():
    # request.form["female"] returns True if select, 
    # else it returns error
    try:
        is_female = request.form["female"]
    except:
        is_female = False

    new_tutor = Tutor(
        first_name=request.form["first_name"],
        last_name= request.form["last_name"],
        age=request.form["age"],
        is_female= is_female,
        email=request.form["email"],
        password=request.form["password"]
    )

    if new_tutor.save():
        flash("Student created!")
        return redirect(url_for('home'))
    else:
        flash("Error creating student!")
        return render_template('home.html', errors = new_student.errors)