from flask import Flask
from .config import app_config
from dotenv import load_dotenv

def create_app(config_name, register_blueprints):
    load_dotenv()
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    if register_blueprints:
        app = register_blueprint(app)
    return app

def register_blueprint(app):
    from proj.api import users

    app.register_blueprint(users.user_bp, url_prefix='/user')
    return app

app = create_app('dev', register_blueprints=True)
