import os
import config
import decimal
import flask.json
from flask import Flask
from flask_wtf import CSRFProtect
from flask_login import LoginManager
from flask_jwt_extended import JWTManager
from models.base_model import db
class MyJSONEncoder(flask.json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            # Convert decimal instances to strings.
            return str(obj)
        return super(MyJSONEncoder, self).default(obj)


web_dir = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), 'aspire_web')

app = Flask('Aspire', root_path=web_dir)
app.json_encoder = MyJSONEncoder
csrf = CSRFProtect(app)
jwt = JWTManager(app)

if os.getenv('FLASK_ENV') == 'production':
    app.config.from_object("config.ProductionConfig")
else:
    app.config.from_object("config.DevelopmentConfig")


@app.before_request
def before_request():
    db.connect()


@app.teardown_request
def _db_close(exc):
    if not db.is_closed():
        print(db)
        print(db.close())
    return exc
