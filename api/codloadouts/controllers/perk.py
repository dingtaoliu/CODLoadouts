from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, jsonify
)
from werkzeug.exceptions import abort

from codloadouts.db import get_db
from codloadouts.models.perk import Perk, PerkType


bp = Blueprint('api.perk', __name__, url_prefix='/api/perks')

# route to get all perks
@bp.route('/', methods=['GET'])
def all_perks():
    perks = Perk.query.all()

    return jsonify([a.serialize for a in perks])


# route to create a perk
@bp.route('/', methods=['POST'])
def create_perk():
    error = None
    perk_type = PerkType[request.form['perk_type']]
    perk_name = request.form['perk_name']

    if not perk_type or not perk_name:
            error = 'perk name and type are required.'
            
    elif Perk.query.filter(
        Perk.perk_type == perk_type and 
        Perk.perk_name == perk_name
        ).first() is not None:
            error = 'perk {} already exists.'.format(perk_name)
    
    if error is None:
        new_perk = Perk(
            perk_type = perk_type,
            perk_name = perk_name
        )

        db.session.add(new_perk)
        db.session.commit()

        return "Created {} successfully".format(new_perk)

    return error


def get_perk(id):
    perk = Perk.query.get(id)

    if perk is None:
        abort(404, "perk id {} doesn't exist.".format(id))

    return perk

# used to update, show, or delete a perk
@bp.route('/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def modify_perk(id):
    perk = get_perk(id)
    error = None

    if request.method == 'PUT':
        perk_type = request.form['perk_type']
        perk_name = request.form['perk_name']
        
        perk.perk_type = perk_type
        perk.perk_name = perk_name

        db.session.commit()

    elif request.method == 'DELETE':
        db.session.delete(perk)
        db.session.commit()

        return "perk id {} deleted successfully".format(id)
    
    return jsonify(perk.serialize)


