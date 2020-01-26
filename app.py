import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object('configurations.DevelopmentConfig')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

from templates.api.controllers.classroom.routes import classroom_blueprint
from templates.api.controllers.problems.routes import problems_blueprint
from templates.api.controllers.quiz.routes import quiz_blueprint
from templates.api.controllers.scores.routes import scores_blueprint
from templates.api.controllers.step.routes import step_blueprint
from templates.api.controllers.student.routes import student_blueprint
from templates.api.controllers.teacher.routes import teacher_blueprint
from templates.api.controllers.users.routes import users_blueprint

# register the blueprints
app.register_blueprint(classroom_blueprint)
app.register_blueprint(problems_blueprint)
app.register_blueprint(quiz_blueprint)
app.register_blueprint(scores_blueprint)
app.register_blueprint(step_blueprint)
app.register_blueprint(student_blueprint)
app.register_blueprint(teacher_blueprint)
app.register_blueprint(users_blueprint)

@app.errorhandler(404)
def not_found(e):
    return "Oops! This endpoint isn't ready yet. Try again in V2"

if __name__ == '__main__':
    app.run()