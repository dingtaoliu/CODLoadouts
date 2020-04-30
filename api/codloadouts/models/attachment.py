from codloadouts import db   
from enum import Enum 

class AttachmentType(Enum):
    MUZZLE = 'muzzle'
    BARREL = 'barrel'
    LASER = 'laser'
    OPTIC = 'optic'
    STOCK = 'stock'
    UNDERBARREL = 'underbarrel'
    AMMUNITION = 'ammunition'
    REAR_GRIP = 'rear grip'
    PERK = 'perk'

class Attachment(db.Model):

    __tablename__ = 'attachment'
    id = db.Column(db.Integer, primary_key=True)

    attachment_type = db.Column(db.Enum(AttachmentType), index=True, unique=False, nullable=False)

    attachment_name = db.Column(db.Text, index=False, unique=False, nullable=False)

    @property
    def serialize(self):
        return {
            'attachment_type': self.attachment_type.value,
            'attachment_name': self.attachment_name
            }

    def __repr__(self):
        return '<Attachment {}: {}>'.format(self.attachment_type.value, self.attachment_name)

