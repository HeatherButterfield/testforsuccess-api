from flask import render_template, Blueprint
users_blueprint = Blueprint('users_controller', __name__)

# a Python object (dict):
users_mock = {
    1: {
        "first_name": "John",
        "last_name": "Doe"
    },
    2: {
        "first_name": "Jane",
        "last_name": "Doe"
    }
}

@users_blueprint.route('/api/users/', methods=['GET'])
def index():
    return users_mock

@users_blueprint.route('/api/users/<int:user_id>', methods=['GET'])
def getUserById(user_id):
    user = users_mock.get(user_id)
    if user != None:
        return user
    else:
        return "Oops! That user does not exist"