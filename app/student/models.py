from app import db, ma

class Student(db.Model):
    """Model for Student accounts."""

    __tablename__ = 'student'
    id = db.Column(db.Integer, primary_key=True)
    teacher_id = db.Column(db.Integer)
    class_id = db.Column(db.String(64))
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))

class StudentSchema(ma.ModelSchema):
    class Meta:
        model = Student
        sqla_session = db.session