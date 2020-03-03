from flask import render_template, Blueprint
problems_blueprint = Blueprint('problems_controller', __name__)

@problems_blueprint.route('/api/problems/', methods=['GET'])
def index():
    return "This is to be built later"