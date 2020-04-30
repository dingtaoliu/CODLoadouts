from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, jsonify
)
from werkzeug.exceptions import abort

from codloadouts.db import get_db
from codloadouts.models.weapon import Weapon, WeaponType


bp = Blueprint('api.weapon', __name__, url_prefix='/api/weapons')

# route to get all weapons
@bp.route('/', methods=['GET'])
def all_weapons():
    weapons = Weapon.query.all()

    return jsonify([a.serialize for a in weapons])


# route to create a weapon
@bp.route('/', methods=['POST'])
def create_weapon():
    error = None
    weapon_type = WeaponType[request.form['weapon_type']]
    weapon_name = request.form['weapon_name']

    if not weapon_type or not weapon_name:
            error = 'weapon name and type are required.'
            
    elif Weapon.query.filter(
        Weapon.weapon_type == weapon_type and 
        Weapon.weapon_name == weapon_name
        ).first() is not None:
            error = 'weapon {} already exists.'.format(weapon_name)
    
    if error is None:
        new_weapon = Weapon(
            weapon_type = weapon_type,
            weapon_name = weapon_name
        )

        db.session.add(new_weapon)
        db.session.commit()

        return "Created {} successfully".format(new_weapon)

    return error


def get_weapon(id):
    weapon = Weapon.query.get(id)

    if weapon is None:
        abort(404, "weapon id {} doesn't exist.".format(id))

    return weapon

# used to update, show, or delete a weapon
@bp.route('/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def modify_weapon(id):
    weapon = get_weapon(id)
    error = None

    if request.method == 'PUT':
        weapon_type = request.form['weapon_type']
        weapon_name = request.form['weapon_name']
        
        weapon.weapon_type = weapon_type
        weapon.weapon_name = weapon_name

        db.session.commit()

    elif request.method == 'DELETE':
        db.session.delete(weapon)
        db.session.commit()

        return "weapon id {} deleted successfully".format(id)
    
    return jsonify(weapon.serialize)


