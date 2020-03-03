from flask import render_template, Blueprint
scores_blueprint = Blueprint('scores_controller', __name__)

@scores_blueprint.route('/api/scores/', methods=['GET'])
def index():
    return "This is to be built later"