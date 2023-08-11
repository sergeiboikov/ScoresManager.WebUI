from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import smgr_config as cfg
import constants as cst

smgr_cfg = cfg.Config(cst.SMGR_CFG_FILE)

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = cst.SMGR_APP_KEY
    app.config['SQLALCHEMY_DATABASE_URI'] = smgr_cfg.PG_DB_CONNECTION_SQLALCHEMY_URI
    db.init_app(app)

    from .views import views_blueprint
    from .auth import auth_blueprint
    from .scores import scores_blueprint
    from .courses import courses_blueprint

    app.register_blueprint(views_blueprint, url_prefix='/')
    app.register_blueprint(auth_blueprint, url_prefix='/')
    app.register_blueprint(scores_blueprint, url_prefix='/')
    app.register_blueprint(courses_blueprint, url_prefix='/')

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
