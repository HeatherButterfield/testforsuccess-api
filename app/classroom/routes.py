from flask import render_template
from flask import Blueprint, jsonify, request, abort
from .models import Classroom, ClassSchema
from app import db
classroom_blueprint = Blueprint('classroom_controller', __name__)

@classroom_blueprint.route('/api/classroom/getAllClasses/', methods=['GET'])
def getAllClasses():
    classes = Classroom.query \
        .all()

    class_schema = ClassSchema(many=True)
    return jsonify(class_schema.dump(classes))

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
