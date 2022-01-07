from flask import Blueprint, jsonify, request
from ..models import Automobile, autos_schema, auto_schema, db

autos_bp = Blueprint('autos_bp', __name__)

@autos_bp.route('/')
def index():
    autos = Automobile.query.all()
    return jsonify(autos_schema.dump(autos))



@autos_bp.route('/<int:auto_id>')
def show(auto_id):
    auto = Automobile.query.get(auto_id)

    if not auto:
        return { 'message': 'No automobile with that id' }, 404

    return auto_schema.dump(auto)



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



@autos_bp.route('/<int:auto_id>', methods=['PATCH'])
def update(auto_id):
    auto = Automobile.query.get(auto_id)
    json_data = request.json
    available_fields = ('make', 'model', 'color', 'year')

    if not auto:
        return { 'message': 'No automobile with that id' }, 404

    for field in available_fields:
        if field in json_data:
            setattr(auto, field, json_data[field])

    db.session.commit()
    return auto_schema.dump(auto)


@autos_bp.route('/<int:auto_id>', methods=['DELETE'])
def delete(auto_id):
    auto = Automobile.query.get(auto_id)

    db.session.delete(auto)
    db.session.commit()

    return '', 204
