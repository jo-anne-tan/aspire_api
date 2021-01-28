from flask import Blueprint, flash, render_template,request,redirect,url_for,session,abort
from models.subject import Subject

subjects_blueprint = Blueprint('subjects',
                            __name__,
                            template_folder='templates')

@subjects_blueprint.route('/new', methods=['GET'])
def new():
    return render_template('subjects/new.html')

@subjects_blueprint.route('/create/<cat>/<desc>', methods=['POST'])
def create(cat,desc):
    s = Subject(
        category=cat,
        description=desc
    )

    if s.save():
        flash("Subject created")
