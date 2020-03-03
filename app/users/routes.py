from flask import render_template, Blueprint, request
users_blueprint = Blueprint('users_controller', __name__)
from .models import User, db

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
    users = db.session.query(User).all()
    print(users)
    return users_mock

@users_blueprint.route('/api/users/<int:user_id>', methods=['GET'])
def getUserById(user_id):
    user = users_mock.get(user_id)
    if user != None:
        return user
    else:
        return "Oops! That user does not exist"

@users_blueprint.route('/api/users/', methods=['POST'])
def newUser():
    if not request.json or not 'first_name' or not 'last_name' in request.json:
        abort(400)

    new_user = User(first_name='Test',
                    last_name='Test2')
    #testing
    db.session.add(new_user)  # Adds new User record to database
    db.session.commit()  # Commits all changes
    return request.json

# @users_blueprint.route('/api/users/<int:user_id', methods=['PUT'])
# def updateUser():
#
# @users_blueprint.route('api/users/<int:user_id', methods=['DELETE'])
# def deleteUser():