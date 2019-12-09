from flask import render_template, Blueprint
api_blueprint = Blueprint('api',__name__)

@api_blueprint.route('/api/hello')
def index():
        return "Hello World"

# app name 
@api_blueprint.errorhandler(404) 
def not_found(e): 
  return "Oops! This route is not build yet. Try again in V2"
