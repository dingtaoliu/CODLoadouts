from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, jsonify
)
from werkzeug.exceptions import abort

from codloadouts import db
from codloadouts.models.attachment import Attachment

bp = Blueprint('api.attachment', __name__, url_prefix='/api/attachment')

# route to get all equipments
@bp.route('/', methods=['GET'])
def all_attachments():
    attachments = Attachment.query.all()

    return jsonify([a.serialize for a in attachments])


# route to create a equipment
@bp.route('/', methods=['POST'])
def create_attachment():
    error = None
    attachment_type = request.form['attachment_type']
    attachment_name = request.form['attachment_name']

    if not attachment_type or not attachment_name:
            error = 'attachment name and type are required.'
            
    elif Attachment.query.filter(
        Attachment.attachment_type == attachment_type and 
        Attachment.attachment_name == attachment_name
        ).first() is not None:
            error = 'attachment {} already exists.'.format(attachment_name)
    
    if error is None:
        new_attachment = Attachment(
            attachment_type = attachment_type,
            attachment_name = attachment_name
        )

        db.session.add(new_attachment)
        db.session.commit()

        return "Created {} successfully".format(new_attachment)

    return error

def get_attachment(id):
    attachment = Attachment.query.get(id)

    if attachment is None:
        abort(404, "attachment id {} doesn't exist.".format(id))

    return attachment

# used to update, show, or delete a equipment
@bp.route('/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def modify_attachment(id):
    attachment = get_attachment(id)
    error = None

    if request.method == 'PUT':
        attachment_type = request.form['attachment_type']
        attachment_name = request.form['attachment_name']
        
        attachment.attachment_type = attachment_type
        attachment.attachment_name = attachment_name

        db.session.commit()

        equipment = get_equipment(id)
    elif request.method == 'DELETE':
        db.session.delete(attachment)
        db.session.commit()

        return "attachment id {} deleted successfully".format(id)
    
    return jsonify(attachment.serialize)


