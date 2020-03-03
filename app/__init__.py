from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    #Initialize the core application
    app = Flask(__name__)
    app.config.from_object('configurations.DevelopmentConfig')
    db.init_app(app)
    #Initialize Plugins
    with app.app_context():
        from .classroom.routes import classroom_blueprint
        from .problems.routes import problems_blueprint
        from .quiz.routes import quiz_blueprint
        from .scores.routes import scores_blueprint
        from .step.routes import step_blueprint
        from .student.routes import student_blueprint
        from .teacher.routes import teacher_blueprint
        from .users.routes import users_blueprint

        db.create_all()
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

    return app