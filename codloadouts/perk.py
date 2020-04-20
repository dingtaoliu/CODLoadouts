from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, jsonify
)
from werkzeug.exceptions import abort

from codloadouts.db import get_db

bp = Blueprint('api.perk', __name__, url_prefix='/api/perk')

# route to get all perks
@bp.route('/', methods=['GET'])
def all_perks():
    db = get_db()
    perks = db.execute(
        'SELECT * FROM perk'
    ).fetchall() 

    return jsonify([dict(wep) for wep in perks])


# route to create a perk
@bp.route('/', methods=['POST'])
def create_perk():
    db = get_db()
    error = None
    perk_name = request.form['perk_name']

    if not perk_name:
            error = 'perk name is required.'
    elif db.execute(
            'SELECT id FROM perk WHERE perk_name = ?', (perk_name,)
        ).fetchone() is not None:
            error = 'perk {} already exists.'.format(perk_name)
    
    if error is None:
        db.execute(
            'INSERT INTO perk (perk_name) VALUES (?)',
            (perk_name,)
        )
        db.commit()

        return "Created perk {} successfully".format(perk_name)

    return error


def get_perk(id):
    perk = get_db().execute(
        'SELECT * FROM perk WHERE id = ?',
        (id,)
    ).fetchone()

    if perk is None:
        abort(404, "perk id {} doesn't exist.".format(id))

    return perk

# used to update, show, or delete a perk
@bp.route('/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def modify_perk(id):
    perk = get_perk(id)
    db = get_db()
    error = None

    if request.method == 'PUT':
        perk_name = request.form['perk_name']
        db.execute(
            'UPDATE perk SET perk_name = ? WHERE id = ?',
            (perk_name, id)
        )
        db.commit()

        perk = get_perk(id)
    elif request.method == 'DELETE':
        db.execute(
            'DELETE FROM perk WHERE id = ?',
            (id,)
        )
        db.commit()

        return "perk id {} deleted successfully".format(id)
    
    return jsonify(dict(perk))


