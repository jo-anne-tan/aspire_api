from app import app
from flask import render_template
from .util.assets import bundles
from flask_assets import Environment, Bundle
from aspire_web.blueprints.tutors.views import tutors_blueprint
from aspire_web.blueprints.students.views import students_blueprint
from aspire_web.blueprints.subjects.views import subjects_blueprint
from aspire_web.blueprints.tutor_sessions.views import tutor_sessions_blueprint
from aspire_web.blueprints.student_tutor_sessions.views import student_tutor_sessions_blueprint

assets = Environment(app)
assets.register(bundles)

app.register_blueprint(tutors_blueprint, url_prefix="/tutors")
app.register_blueprint(students_blueprint, url_prefix="/students")
app.register_blueprint(subjects_blueprint, url_prefix="/subjects")
app.register_blueprint(tutor_sessions_blueprint, url_prefix="/tutor_sessions")
app.register_blueprint(student_tutor_sessions_blueprint, url_prefix="/student_tutor_sessions")


@app.route('/')
def home():
    return render_template('home.html')