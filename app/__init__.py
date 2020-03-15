import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

basedir = os.path.abspath(os.path.dirname(__file__))
# app = Flask(__name__, template_folder='templates')
app = Flask(__name__)
app.config.from_object('configurations.DevelopmentConfig')
db = SQLAlchemy(app)
ma = Marshmallow(app)
db.create_all()
# import all blueprints
from .classroom.routes import classroom_blueprint
from .problems.routes import problems_blueprint
from .quiz.routes import quiz_blueprint
from .scores.routes import scores_blueprint
from .step.routes import step_blueprint
from .student.routes import student_blueprint
from .teacher.routes import teacher_blueprint
from .default.routes import default_blueprint

# register the blueprints
app.register_blueprint(classroom_blueprint)
app.register_blueprint(problems_blueprint)
app.register_blueprint(quiz_blueprint)
app.register_blueprint(scores_blueprint)
app.register_blueprint(step_blueprint)
app.register_blueprint(student_blueprint)
app.register_blueprint(teacher_blueprint)
app.register_blueprint(default_blueprint)