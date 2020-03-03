from flask import render_template, Blueprint
quiz_blueprint = Blueprint('quiz_controller', __name__)

@quiz_blueprint.route('/api/quiz/', methods=['GET'])
def index():
    return "This is to be built later"