from flask import Blueprint, flash, render_template,request,redirect,url_for,session,abort

tutors_blueprint = Blueprint('tutors',
                            __name__,
                            template_folder='templates')

@tutors_blueprint.route('/new', methods=['GET'])
def new():
    return render_template('tutors/new.html')
