from flask import Blueprint, jsonify, request, abort
from .models import Student, StudentSchema
from app import db

student_blueprint = Blueprint('student_controller', __name__)

@student_blueprint.route('/api/student/getAllStudents/', methods=['GET'])
def getAllStudents():
    students = Student.query \
        .all()

    student_schema = StudentSchema(many=True)
    return jsonify(student_schema.dump(students))

@student_blueprint.route('/api/student/getStudentById/<int:student_id>', methods=['GET'])
def getStudentById(student_id):
    student = Student.query \
        .filter(Student.id == student_id) \
        .one_or_none()

    if student is not None:
        student_schema = StudentSchema()
        return jsonify(student_schema.dump(student))
    else:
        abort(404, 'Student not found for Id: {student_id}'.format(student_id=student_id))

@student_blueprint.route('/api/student/getStudentsByFacultyId/<int:teacher_id>', methods=['GET'])
def getStudentsByFacultyId(teacher_id):
    students = Student.query \
        .filter(Student.teacher_id == teacher_id) \
        .all()

    if students is not None:
        student_schema = StudentSchema(many=True)
        return jsonify(student_schema.dump(students))
    else:
        abort(404, 'Students not found for Id: {teacher_id}'.format(teacher_id=teacher_id))

@student_blueprint.route('/api/student/getStudentsByClassId/<int:class_id>', methods=['GET'])
def getStudentsByClassId(class_id):
    students = Student.query \
        .filter(Student.class_id == class_id) \
        .all()

    if students is not None:
        student_schema = StudentSchema(many=True)
        return jsonify(student_schema.dump(students))
    else:
        abort(404, 'Students not found for Id: {class_id}'.format(class_id=class_id))

@student_blueprint.route('/api/student/saveStudent/', methods=['PUT'])
def saveStudent():
    student = request.get_json()
    teacher_id = student.get('teacher_id')
    fname = student.get('first_name')
    lname = student.get('last_name')
    classId = student.get('class_id')

    existing_student = Student.query \
        .filter(Student.first_name == fname) \
        .filter(Student.last_name == lname) \
        .filter(Student.teacher_id == teacher_id) \
        .filter(Student.class_id == classId) \
        .one_or_none()

    if existing_student is None:
        schema = StudentSchema()
        new_student = schema.load(student, session=db.session)

        db.session.add(new_student)
        db.session.commit()

        return jsonify({'Result': 'Success'}), 200
    else:
        abort(404, f'Student: {fname} {lname} exists already')

@student_blueprint.route("/api/student/updateStudent/<int:student_id>", methods=['PUT'])
def updateStudent(student_id):
    update_student = Student.query \
        .filter(Student.id == student_id) \
        .one_or_none()

    req = request.get_json()
    teacher_id = req.get('teacher_id')
    fname = req.get('first_name')
    lname = req.get('last_name')
    classId = req.get('class_id')
    existing_student = Student.query \
        .filter(Student.first_name == fname) \
        .filter(Student.last_name == lname) \
        .filter(Student.teacher_id == teacher_id) \
        .filter(Student.class_id == classId) \
        .one_or_none()

    if update_student is None:
        abort(404, 'Student not found for Id: {student_id}'.format(student_id=student_id))
    elif (existing_student is not None and existing_student.id != student_id):
        abort(404, f'Student: {student_id} - {fname} {lname} exists already')
    else:
        schema = StudentSchema()
        update = schema.load(req, session=db.session)

        update.id = update_student.id

        db.session.merge(update)
        db.session.commit()

        return jsonify({'Result': 'Success'}), 200

@student_blueprint.route("/api/student/deleteStudent/<int:student_id>", methods=['DELETE'])
def deleteStudent(student_id):
    student = Student.query \
        .filter(Student.id == student_id) \
        .one_or_none()

    if student is not None:
        db.session.delete(student)
        db.session.commit()
        return jsonify({'Result': 'Success'}), 200
    else:
        abort(404, 'Student not found for Id: {student_id}'.format(student_id=student_id))
