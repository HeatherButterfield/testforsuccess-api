from app import db, ma

class Teacher(db.Model):
    """Model for Teacher accounts."""

    __tablename__ = 'teacher'
    id = db.Column(db.Integer, primary_key=True)
    faculty_id = db.Column(db.Integer, unique=True)
    password = db.Column(db.String(64), unique=True)
    first_name = db.Column(db.String(64), unique=True)
    last_name = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(64), unique=True)

class TeacherSchema(ma.ModelSchema):
    class Meta:
        model = Teacher
        sqla_session = db.session