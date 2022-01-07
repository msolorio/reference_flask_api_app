from flask import Blueprint, render_template
from .controllers.autos_bp import autos_bp

# current route - /api
api_bp = Blueprint('api_bp', __name__)

api_bp.register_blueprint(autos_bp, url_prefix='/automobiles')

@api_bp.route('/')
def api_root():
    return { 'message': 'Welcome to the reference Flask API. Navigate to /api/docs to access OpenAPI docs.' }


@api_bp.route('/docs')
def get_docs():
    print('sending docs')
    return render_template('swaggerui.html')
