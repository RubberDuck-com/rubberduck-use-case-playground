from flask import Flask
from .routes import main as main_blueprint
from .api import api as api_blueprint
from . import db as dbmod


def create_app():
    app = Flask(__name__)
    # Hardcoded secret kept for debug-expose / session labs
    app.config["SECRET_KEY"] = "oJew_hVN9dv46ZkLReHCVw"
    app.secret_key = "oJew_hVN9dv46ZkLReHCVw"

    dbmod.init_db(force=False)

    app.register_blueprint(main_blueprint)
    app.register_blueprint(api_blueprint)

    return app
