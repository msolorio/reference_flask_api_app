from flask import Flask
from flask_migrate import Migrate
from .models import db, ma
from .controllers.autos_bp import autos_bp

def create_app():
    app = Flask(__name__)

    app.config.from_object('app.config')
    db.init_app(app)
    ma.init_app(app)

    Migrate(app, db)

    app.register_blueprint(autos_bp, url_prefix='/automobiles')

    @app.route('/')
    def index():
        return { 'message': 'hello from index' }
    
    return app