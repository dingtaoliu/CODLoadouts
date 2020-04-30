from codloadouts import db   

class WeaponLoadout(db.Model):

    __tablename__ = 'weapon_loadout'
    id = db.Column(db.Integer, primary_key=True)

    weapon_loadout_name = db.Column(db.Text, index=False, unique=False, nullable=False)

    # foreign keys
    weapon_id = db.Column(db.Integer, db.ForeignKey('weapon.id'), unique=False, nullable=False)
    attachment_1_id = db.Column(db.Integer, db.ForeignKey('attachment.id'), unique=False, nullable=True)
    attachment_2_id = db.Column(db.Integer, db.ForeignKey('attachment.id'), unique=False, nullable=True)
    attachment_3_id = db.Column(db.Integer, db.ForeignKey('attachment.id'), unique=False, nullable=True)
    attachment_4_id = db.Column(db.Integer, db.ForeignKey('attachment.id'), unique=False, nullable=True)
    attachment_5_id = db.Column(db.Integer, db.ForeignKey('attachment.id'), unique=False, nullable=True)

    # time stamps
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    # relations 
    weapon = db.relationship('Weapon')
    attachment_1 = db.relationship('Attachment', foreign_keys=[attachment_1_id])
    attachment_2 = db.relationship('Attachment', foreign_keys=[attachment_2_id])
    attachment_3 = db.relationship('Attachment', foreign_keys=[attachment_3_id])
    attachment_4 = db.relationship('Attachment', foreign_keys=[attachment_4_id])
    attachment_5 = db.relationship('Attachment', foreign_keys=[attachment_5_id])

    attachments = [
        attachment_1, 
        attachment_2, 
        attachment_3, 
        attachment_4, 
        attachment_5
    ]

    __table_args__ = (db.UniqueConstraint('attachment_1_id', 'attachment_2_id', 'attachment_3_id', 'attachment_4_id', 'attachment_5_id'),)

    @property
    def serialize(self):
        return {
            'weapon_loadout_name': self.weapon_loadout_name,
            'weapon': self.weapon.serialize(),
            'attachment_1': self.attachment_1.serialize() if self.attachment_1 else None
            }

    def __repr__(self):
        a1 = self.attachment_1.attachment_name if self.attachment_1 else None 
        a2 = self.attachment_2.attachment_name if self.attachment_2 else None 
        return '<Weapon Loadout {}: {}, {}, {}>'.format(self.weapon_loadout_name, self.weapon.weapon_name, a1, a2)  