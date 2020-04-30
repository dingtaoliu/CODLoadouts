from codloadouts import db     
from enum import Enum 

class PerkType(Enum):
    BLUE = 'blue'
    RED = 'red'
    YELLOW = 'yellow'

class Perk(db.Model):

    __tablename__ = 'perk'
    id = db.Column(db.Integer, primary_key=True)

    perk_type = db.Column(db.Enum(PerkType), index=True, unique=False, nullable=False)

    perk_name = db.Column(db.Text, index=False, unique=False, nullable=False)

    @property
    def serialize(self):
        return {
            'perk_type': self.perk_type.value,
            'perk_name': self.perk_name
            }

    def __repr__(self):
        return '<Perk {}: {}>'.format(self.perk_type.value, self.perk_name)

