from flask import Flask, jsonify, render_template
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
    def index():
        return { 'message': 'hello from index' }
    
    @app.route('/docs')
    def get_docs():
        print('sending docs')
        return render_template('swaggerui.html')

    return app