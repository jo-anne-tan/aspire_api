from flask import Blueprint, flash, render_template,request,redirect,url_for,session,abort

students_blueprint = Blueprint('students',
                            __name__,
                            template_folder='templates')


@students_blueprint.route('/new', methods=['GET'])
def new():
    return render_template('students/new.html')
