from app import app
from .util.assets import bundles
from flask_assets import Environment, Bundle


assets = Environment(app)
assets.register(bundles)

@app.route('/', methods=['GET'])
def home():
    return "ASPIRE WEB FOR API TEST"