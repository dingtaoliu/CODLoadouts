from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, jsonify
)
from werkzeug.exceptions import abort

from codloadouts.db import get_db
from codloadouts.models.equipment import Equipment, EquipmentType


bp = Blueprint('api.equipment', __name__, url_prefix='/api/equipments')

# route to get all equipments
@bp.route('/', methods=['GET'])
def all_equipments():
    equipments = Equipment.query.all()

    return jsonify([a.serialize for a in equipments])


# route to create a equipment
@bp.route('/', methods=['POST'])
def create_equipment():
    error = None
    equipment_type = EquipmentType[request.form['equipment_type']]
    equipment_name = request.form['equipment_name']

    if not equipment_type or not equipment_name:
            error = 'equipment name and type are required.'
            
    elif Equipment.query.filter(
        Equipment.equipment_type == equipment_type and 
        Equipment.equipment_name == equipment_name
        ).first() is not None:
            error = 'equipment {} already exists.'.format(equipment_name)
    
    if error is None:
        new_equipment = Equipment(
            equipment_type = equipment_type,
            equipment_name = equipment_name
        )

        db.session.add(new_equipment)
        db.session.commit()

        return "Created {} successfully".format(new_equipment)

    return error


def get_equipment(id):
    equipment = Equipment.query.get(id)

    if equipment is None:
        abort(404, "equipment id {} doesn't exist.".format(id))

    return equipment

# used to update, show, or delete a equipment
@bp.route('/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def modify_equipment(id):
    equipment = get_equipment(id)
    error = None

    if request.method == 'PUT':
        equipment_type = request.form['equipment_type']
        equipment_name = request.form['equipment_name']
        
        equipment.equipment_type = equipment_type
        equipment.equipment_name = equipment_name

        db.session.commit()

    elif request.method == 'DELETE':
        db.session.delete(equipment)
        db.session.commit()

        return "equipment id {} deleted successfully".format(id)
    
    return jsonify(equipment.serialize)


