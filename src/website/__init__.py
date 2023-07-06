from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import smgr_config as cfg

smgr_config = cfg.Config(r"src/config/smgr_config.yaml")

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "asdadfsdfe"
    app.config["SQLALCHEMY_DATABASE_URI"] = smgr_config.PG_DB_CONNECTION_SQLALCHEMY_URI
    db.init_app(app)

    from .views import views
    from .auth import auth
    from .scores import scores
    from .courses import courses

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(scores, url_prefix='/')
    app.register_blueprint(courses, url_prefix='/')

    from .models import User

    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app
