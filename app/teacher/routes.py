from flask import render_template, Blueprint, jsonify, request
from app import db
from .models import Teacher
teacher_blueprint = Blueprint('teacher_controller', __name__)

@teacher_blueprint.route('/api/teacher/getAllTeachers/', methods=['GET'])
def getAllTeachers():
    teachers = db.session.query(Teacher).all()
    return jsonify([i.to_dict() for i in teachers])

@teacher_blueprint.route('/api/teacher/getTeacherById/<int:teacher_id>', methods=['GET'])
def getTeacherById(teacher_id):
    teacher = db.session.query(Teacher).get(teacher_id)
    return jsonify(teacher.to_dict())


@teacher_blueprint.route('/api/teacher/getTeacherByFacultyId/<int:faculty_id>', methods=['GET'])
def getTeacherByFacultyId(faculty_id):
    teacher = db.session.query(Teacher).filter(Teacher.faculty_id == faculty_id).first()
    return jsonify(teacher.to_dict())

@teacher_blueprint.route("/api/teacher/updateTeacher/<int:teacher_id>", methods=['PUT'])
def users_update(teacher_id):
    teacher = db.session.query(Teacher).get(teacher_id)
    form = request.get_json()
    if not form.get('teacher'):
        return jsonify({'Error': 'Bad data received'}), 400

    return jsonify({'teacher': teacher.to_dict()}), 200