from flask import Flask

def create_app(config_filename=None):
    app = Flask(__name__)
    if config_filename:
        app.config.from_pyfile(config_filename)

    from .routes import api_bp
    app.register_blueprint(api_bp)

    return app
