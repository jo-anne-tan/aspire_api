from app import app
from flask import render_template
from .util.assets import bundles
from flask_assets import Environment, Bundle
from aspire_web.blueprints.tutors.views import tutors_blueprint
from aspire_web.blueprints.students.views import students_blueprint
from aspire_web.blueprints.subjects.views import subjects_blueprint

assets = Environment(app)
assets.register(bundles)

app.register_blueprint(students_blueprint, url_prefix="/students")
app.register_blueprint(tutors_blueprint, url_prefix="/tutors")
app.register_blueprint(subjects_blueprint, url_prefix="/subjects")


@app.route('/')
def home():
    return render_template('home.html')