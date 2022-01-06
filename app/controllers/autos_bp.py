from flask import Blueprint, jsonify, request
from ..models import Automobile, autos_schema, auto_schema, db

autos_bp = Blueprint('autos_bp', __name__)

@autos_bp.route('/')
def index():
    autos = Automobile.query.all()
    return jsonify(autos_schema.dump(autos))


@autos_bp.route('/', methods=['POST'])
def create():
    json_data = request.json

    required_fields = ('make', 'model', 'year')
    for field in required_fields:
        if not json_data.get(field):
            return f'{field} is a required field', 404

    new_auto = Automobile(
        make=json_data.get('make'),
        model=json_data.get('model'),
        year=json_data.get('year'),
        color=json_data.get('color')
    )

    db.session.add(new_auto)
    db.session.commit()

    return auto_schema.dump(new_auto)
