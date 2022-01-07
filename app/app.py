from flask import Flask, render_template, redirect, url_for
from flask_migrate import Migrate
from .models import db, ma
from .controllers.autos_bp import autos_bp

def create_app():
    app = Flask(__name__)

    app.config.from_object('app.config')
    db.init_app(app)
    ma.init_app(app)

    Migrate(app, db)

    app.register_blueprint(autos_bp, url_prefix='/api/automobiles')

    @app.route('/api/')
    def api_root():
        return { 'message': 'Welcome to the reference Flask API. Navigate to /api/docs to access OpenAPI docs.' }

    @app.route('/')
    def index():
        return redirect(url_for('api_root'))
    
    @app.route('/api/docs')
    def get_docs():
        print('sending docs')
        return render_template('swaggerui.html')

    return app