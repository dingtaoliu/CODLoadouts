from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, jsonify
)
from werkzeug.exceptions import abort

from codloadouts.db import get_db

bp = Blueprint('api.equipment', __name__, url_prefix='/api/equipment')

# route to get all equipments
@bp.route('/', methods=['GET'])
def all_equipments():
    db = get_db()
    equipments = db.execute(
        'SELECT * FROM equipment'
    ).fetchall() 

    return jsonify([dict(wep) for wep in equipments])


# route to create a equipment
@bp.route('/', methods=['POST'])
def create_equipment():
    db = get_db()
    error = None
    equipment_name = request.form['equipment_name']

    if not equipment_name:
            error = 'equipment name is required.'
    elif db.execute(
            'SELECT id FROM equipment WHERE equipment_name = ?', (equipment_name,)
        ).fetchone() is not None:
            error = 'equipment {} already exists.'.format(equipment_name)
    
    if error is None:
        db.execute(
            'INSERT INTO equipment (equipment_name) VALUES (?)',
            (equipment_name,)
        )
        db.commit()

        return "Created equipment {} successfully".format(equipment_name)

    return error


def get_equipment(id):
    equipment = get_db().execute(
        'SELECT * FROM equipment WHERE id = ?',
        (id,)
    ).fetchone()

    if equipment is None:
        abort(404, "equipment id {} doesn't exist.".format(id))

    return equipment

# used to update, show, or delete a equipment
@bp.route('/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def modify_equipment(id):
    equipment = get_equipment(id)
    db = get_db()
    error = None

    if request.method == 'PUT':
        equipment_name = request.form['equipment_name']
        db.execute(
            'UPDATE equipment SET equipment_name = ? WHERE id = ?',
            (equipment_name, id)
        )
        db.commit()

        equipment = get_equipment(id)
    elif request.method == 'DELETE':
        db.execute(
            'DELETE FROM equipment WHERE id = ?',
            (id,)
        )
        db.commit()

        return "equipment id {} deleted successfully".format(id)
    
    return jsonify(dict(equipment))


