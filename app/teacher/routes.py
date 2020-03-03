from flask import render_template, Blueprint
teacher_blueprint = Blueprint('teacher_controller', __name__)

# a Python object (dict):
teacher_mock = {
    1: {
        "user_id": 3,
        "password": "this-is-not-secure"
    },
    2: {
        "user_id": 4,
        "password": "this-is-not-secure"
    }
}

@teacher_blueprint.route('/api/teacher/', methods=['GET'])
def getAllTeachers():
    return teacher_mock

@teacher_blueprint.route('/api/teacher/<int:teacher_id>', methods=['GET'])
def getTeacherById(teacher_id):
    teacher = teacher_mock.get(teacher_id)
    if teacher != None:
        return teacher
    else:
        return "Oops! That teacher does not exist"