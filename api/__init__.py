from app import app, csrf
from flask_cors import CORS

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

## API Routes ##
from api.blueprints.students.views import students_api_blueprint
from api.blueprints.tutors.views import tutors_api_blueprint
from api.blueprints.login.views import login_api_blueprint
from api.blueprints.subjects.views import subjects_api_blueprint

app.register_blueprint(csrf.exempt(students_api_blueprint), url_prefix='/api/v1/students')
app.register_blueprint(csrf.exempt(tutors_api_blueprint), url_prefix='/api/v1/tutors')
app.register_blueprint(csrf.exempt(login_api_blueprint), url_prefix='/api/v1/login')
app.register_blueprint(csrf.exempt(subjects_api_blueprint), url_prefix='/api/v1/subjects')