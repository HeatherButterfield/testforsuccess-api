    __tablename__ = 'class'
    id = db.Column(db.Integer, primary_key=True)
    teacher_id = db.Column(db.Integer, unique=True)
    class_name = db.Column(db.String(64))

class ClassSchema(ma.ModelSchema):
    class Meta:
        model = Class
        sqla_session = db.session
