from flask import Flask
app = Flask(__name__,
        static_folder = './public',
        template_folder="./static")

from templates.api.views import api_blueprint
# register the blueprints
app.register_blueprint(api_blueprint)

@app.errorhandler(404) 
def not_found(e): 
  return "Oops! This endpoint isn't ready yet. Try again in V2"
