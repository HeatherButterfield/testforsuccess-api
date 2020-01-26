from flask import render_template, Blueprint
classroom_blueprint = Blueprint('classroom_controller', __name__)

# a Python object (dict):
classroom_mock = {
    1: {
        "teacher_id": 1,
        "class_name": "Mr. Doe Pre-K",
    },
    2: {
        "teacher_id": 2,
        "class_name": "Mrs. Doe Pre-K",
    }
}

@classroom_blueprint.route('/api/classroom/', methods=['GET'])
def index():
    return classroom_mock

@classroom_blueprint.route('/api/classroom/<int:classroom_id>', methods=['GET'])
def getStudentById(classroom_id):
    classroom = classroom_mock.get(classroom_id)
    if classroom != None:
        return classroom
    else:
        return "Oops! That class does not exist"