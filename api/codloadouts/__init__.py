import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        #DATABASE=os.path.join(app.instance_path, 'codloadouts.sqlite'),
        SQLALCHEMY_DATABASE_URI='sqlite:////' + os.path.join(app.instance_path, 'codloadouts.sqlalchemy'),
        SQLALCHEMY_TRACK_MODIFICATIONS=False
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/')
    def hello():
        return 'sup sweaters'
    
    # register db
    # from . import db
    # db.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all() 

        # register blueprints
        # from . import auth, weapon
        # app.register_blueprint(auth.bp)
        # app.register_blueprint(weapon.bp)

        from .controllers import attachment
        app.register_blueprint(attachment.bp)

        return app