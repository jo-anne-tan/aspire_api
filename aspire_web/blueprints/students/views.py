from flask import Blueprint, flash, render_template,request,redirect,url_for,session,abort

students_blueprint = Blueprint('students',
                            __name__,
                            template_folder='templates')


@students_blueprint.route('/new', methods=['GET'])
def new():
    return render_template('students/new.html')

@students_blueprint.route('/create',methods=["POST"])
def create():
    try:
        new_student = Student(
            first_name=request.forms["first_name"] ,
            last_name= request.forms["last_name"],
            age=request.forms["age"],
            is_female=request.forms["first_name"],
            email=request.forms["first_name"],
            password=request.forms["first_name"],
        )
    except:
        pass
    pass