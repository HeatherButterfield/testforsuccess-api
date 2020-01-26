from flask import render_template, Blueprint
step_blueprint = Blueprint('step_controller', __name__)

@step_blueprint.route('/api/step/', methods=['GET'])
def index():
    return "This is to be built later"