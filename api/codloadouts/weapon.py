from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, jsonify
)
from werkzeug.exceptions import abort

from codloadouts.db import get_db

bp = Blueprint('api.weapon', __name__, url_prefix='/api/weapon')

# route to get all weapons
@bp.route('/', methods=['GET'])
def all_weapons():
    db = get_db()
    weapons = db.execute(
        'SELECT * FROM weapon'
    ).fetchall() 

    return jsonify([dict(wep) for wep in weapons])


# route to create a weapon
@bp.route('/', methods=['POST'])
def create_weapon():
    db = get_db()
    error = None
    weapon_name = request.form['weapon_name']

    if not weapon_name:
            error = 'Weapon name is required.'
    elif db.execute(
            'SELECT id FROM weapon WHERE weapon_name = ?', (weapon_name,)
        ).fetchone() is not None:
            error = 'Weapon {} already exists.'.format(weapon_name)
    
    if error is None:
        db.execute(
            'INSERT INTO weapon (weapon_name) VALUES (?)',
            (weapon_name,)
        )
        db.commit()

        return "Created weapon {} successfully".format(weapon_name)

    return error


def get_weapon(id):
    weapon = get_db().execute(
        'SELECT * FROM weapon WHERE id = ?',
        (id,)
    ).fetchone()

    if weapon is None:
        abort(404, "Weapon id {} doesn't exist.".format(id))

    return weapon

# used to update, show, or delete a weapon
@bp.route('/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def modify_weapon(id):
    weapon = get_weapon(id)
    db = get_db()
    error = None

    if request.method == 'PUT':
        weapon_name = request.form['weapon_name']
        db.execute(
            'UPDATE weapon SET weapon_name = ? WHERE id = ?',
            (weapon_name, id)
        )
        db.commit()

        weapon = get_weapon(id)
    elif request.method == 'DELETE':
        db.execute(
            'DELETE FROM weapon WHERE id = ?',
            (id,)
        )
        db.commit()

        return "weapon id {} deleted successfully".format(id)
    
    return jsonify(dict(weapon))


