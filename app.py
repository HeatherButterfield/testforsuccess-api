import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object('configurations.DevelopmentConfig')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from templates.api.views import api_blueprint
# register the blueprints
app.register_blueprint(api_blueprint)

@app.errorhandler(404)
def not_found(e):
    return "Oops! This endpoint isn't ready yet. Try again in V2"

if __name__ == '__main__':
    app.run()