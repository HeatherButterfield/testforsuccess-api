from flask import render_template, Blueprint
student_blueprint = Blueprint('student_controller', __name__)

# a Python object (dict):
student_mock = {
    1: {
        "user_id": 1,
        "teacher_id": 1,
        "test_date": "2020/01/26",
        "class_id": 1
    },
    2: {
        "user_id": 2,
        "teacher_id": 1,
        "test_date": "2020/01/26",
        "class_id": 1
    }
}

@student_blueprint.route('/api/student/', methods=['GET'])
def index():
    return student_mock

@student_blueprint.route('/api/student/<int:student_id>', methods=['GET'])
def getStudentById(student_id):
    student = student_mock.get(student_id)
    if student != None:
        return student
    else:
        return "Oops! That student does not exist"