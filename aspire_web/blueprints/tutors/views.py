from flask import Blueprint, flash, render_template,request,redirect,url_for,session,abort
from models.tutor import Tutor
import boto3, botocore
from config import Config
from api.util.helpers import upload_file_to_s3
from werkzeug.utils import secure_filename

S3_KEY=Config.S3_KEY
S3_SECRET=Config.S3_SECRET
S3_BUCKET=Config.S3_BUCKET
S3_LOCATION=Config.S3_LOCATION


tutors_blueprint = Blueprint('tutors',
                            __name__,
                            template_folder='templates')

# @tutors_blueprint.route('/create')
# def create():

#     new_tutor = Tutor(
#         first_name="Jane",
#         last_name= "Doe",
#         age=34,
#         is_female= True,
#         email= 'ABC4@gmail.com',
#         password='ABC4@gmail.com',
#     )

#     if new_tutor.save():
#         flash("Tutor created!")

#         # updating username
#         username = new_tutor.first_name+new_tutor.last_name+str(new_tutor.id)
#         new_tutor.username=username
#         new_tutor.save()

#         return redirect(url_for('home'))
#     else:
#         flash("Unable to create Tutor!")
#         return render_template('home.html', errors = new_tutor.errors)

@tutors_blueprint.route('/profile-photo')
def upload_profile():
    return render_template('tutors/profile_photo.html')

@tutors_blueprint.route('/profile-photo', methods=['POST'])
def upload():
    tutor = Tutor.get_by_id(1) #hard coded for testing purposes

    file = request.files["profile_photo"]
    file.filename = secure_filename(file.filename)
    image_path = upload_file_to_s3(file, "tutor", tutor.username)

    # save photo url in database
    tutor.profile_image=image_path

    if tutor.save(only=[Tutor.profile_image]):
        flash("Profile photo saved to database successfully!",'info')
    else:
        flash("Unable to save profile photo to database.",'danger')
    return render_template('home.html',errors=tutor.errors)