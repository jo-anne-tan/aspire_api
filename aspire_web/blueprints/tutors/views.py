from flask import Blueprint, flash, render_template,request,redirect,url_for,session,abort
from models.tutor import Tutor

tutors_blueprint = Blueprint('tutors',
                            __name__,
                            template_folder='templates')

@tutors_blueprint.route('/create')
def create():

    new_tutor = Tutor(
        first_name="Jane",
        last_name= "Doe",
        age=34,
        is_female= True,
        email= 'ABC4@gmail.com',
        password='ABC4@gmail.com',
    )

    if new_tutor.save():
        flash("Tutor created!")
        
        # updating username
        username = new_tutor.first_name+new_tutor.last_name+str(new_tutor.id)
        new_tutor.username=username
        new_tutor.save()

        return redirect(url_for('home'))
    else:
        flash("Unable to create Tutor!")
        return render_template('home.html', errors = new_tutor.errors)