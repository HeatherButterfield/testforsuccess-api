from flask import Blueprint, jsonify, request, abort
from .models import Teacher, TeacherSchema
from app import db

teacher_blueprint = Blueprint('teacher_controller', __name__)

@teacher_blueprint.route('/api/teacher/getAllTeachers/', methods=['GET'])
def getAllTeachers():
    teachers = Teacher.query \
        .all()

    teacher_schema = TeacherSchema(many=True)
    return jsonify(teacher_schema.dump(teachers))

@teacher_blueprint.route('/api/teacher/getTeacherById/<int:teacher_id>', methods=['GET'])
def getTeacherById(teacher_id):
    teacher = Teacher.query \
        .filter(Teacher.id == teacher_id) \
        .one_or_none()

    if teacher is not None:
        teacher_schema = TeacherSchema()
        return jsonify(teacher_schema.dump(teacher))
    else:
        abort(404, 'Teacher not found for Id: {teacher_id}'.format(teacher_id=teacher_id))

@teacher_blueprint.route('/api/teacher/getTeacherByFacultyId/<int:faculty_id>', methods=['GET'])
def getTeacherByFacultyId(faculty_id):
    teacher = Teacher.query \
        .filter(Teacher.faculty_id == faculty_id) \
        .one_or_none()

    if teacher is not None:
        teacher_schema = TeacherSchema()
        return jsonify(teacher_schema.dump(teacher))
    else:
        abort(404, 'Teacher not found for Id: {faculty_id}'.format(faculty_id=faculty_id))

@teacher_blueprint.route('/api/teacher/saveTeacher/', methods=['PUT'])
def saveTeacher():
    teacher = request.get_json()
    faculty_id = teacher.get('faculty_id')
    fname = teacher.get('first_name')
    lname = teacher.get('last_name')

    existing_teacher = Teacher.query \
        .filter(Teacher.first_name == fname) \
        .filter(Teacher.last_name == lname) \
        .filter(Teacher.faculty_id == faculty_id) \
        .one_or_none()

    if existing_teacher is None:
        schema = TeacherSchema()
        new_teacher = schema.load(teacher, session=db.session)

        db.session.add(new_teacher)
        db.session.commit()

        return jsonify({'Result': 'Success'}), 200
    else:
        abort(404, f'Faculty Member: {faculty_id} - {fname} {lname} exists already')

@teacher_blueprint.route("/api/teacher/updateTeacher/<int:teacher_id>", methods=['PUT'])
def updateTeacher(teacher_id):
    update_teacher = Teacher.query \
        .filter(Teacher.id == teacher_id) \
        .one_or_none()

    req = request.get_json()
    faculty_id = req.get('faculty_id')
    fname = req.get('first_name')
    lname = req.get('last_name')
    existing_teacher = Teacher.query \
        .filter(Teacher.first_name == fname) \
        .filter(Teacher.last_name == lname) \
        .filter(Teacher.faculty_id == faculty_id) \
        .one_or_none()

    if update_teacher is None:
        abort(404, 'Teacher not found for Id: {teacher_id}'.format(teacher_id=teacher_id))
    elif (existing_teacher is not None and existing_teacher.id != teacher_id):
        abort(404, f'Teacher: {teacher_id} - {fname} {lname} exists already')
    else:
        schema = TeacherSchema()
        update = schema.load(req, session=db.session)

        update.id = update_teacher.id

        db.session.merge(update)
        db.session.commit()

        return jsonify({'Result': 'Success'}), 200

@teacher_blueprint.route("/api/teacher/deleteTeacher/<int:teacher_id>", methods=['DELETE'])
def deleteTeacher(teacher_id):
    teacher = Teacher.query \
        .filter(Teacher.id == teacher_id) \
        .one_or_none()

    if teacher is not None:
        db.session.delete(teacher)
        db.session.commit()
        return jsonify({'Result': 'Success'}), 200
    else:
        abort(404, 'Teacher not found for Id: {teacher_id}'.format(teacher_id=teacher_id))
