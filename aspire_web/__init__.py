from app import app
from flask import render_template
from .util.assets import bundles
from flask_assets import Environment, Bundle

assets = Environment(app)
assets.register(bundles)

@app.route('/')
def home():
    return render_template('home.html')