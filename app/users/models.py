from . import db

class User(db.Model):
    """Model for user accounts."""

    __tablename__ = 'users'
    id = db.Column(db.Integer,
                   primary_key=True)
    first_name = db.Column(db.String(64),
                         index=False,
                         unique=True,
                         nullable=False)
    last_name = db.Column(db.String(64),
                               index=False,
                               unique=True,
                               nullable=False)

    def __repr__(self):
        return '<User {}>'.format(self.id)