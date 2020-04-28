from codloadouts import db     
from enum import Enum 

class WeaponType(Enum):
    PRIMARY = 'primary'
    SECONDARY = 'secondary'

class Weapon(db.Model):

    __tablename__ = 'weapon'
    id = db.Column(db.Integer, primary_key=True)

    weapon_type = db.Column(db.Enum(WeaponType), index=True, unique=False, nullable=False)

    weapon_name = db.Column(db.Text, index=False, unique=False, nullable=False)

    @property
    def serialize(self):
        return {
            'weapon_type': self.weapon_type.value,
            'weapon_name': self.weapon_name
            }

    def __repr__(self):
        return '<Weapon {}: {}>'.format(self.weapon_type.value, self.weapon_name)

