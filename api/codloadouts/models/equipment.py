from codloadouts import db     
from enum import Enum 

class EquipmentType(Enum):
    LETHAL = 'lethal'
    TACTICAL = 'tactical'

class Equipment(db.Model):

    __tablename__ = 'equipment'
    id = db.Column(db.Integer, primary_key=True)

    equipment_type = db.Column(db.Enum(EquipmentType), index=True, unique=False, nullable=False)

    equipment_name = db.Column(db.Text, index=False, unique=False, nullable=False)

    @property
    def serialize(self):
        return {
            'equipment_type': self.equipment_type.value,
            'equipment_name': self.equipment_name
            }

    def __repr__(self):
        return '<Equipment {}: {}>'.format(self.equipment_type.value, self.equipment_name)

