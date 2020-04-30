from codloadouts import create_app   
from flask_sqlalchemy import SQLAlchemy

app = create_app()
db = SQLAlchemy(app)

from codloadouts.models.attachment import * 
from codloadouts.models.weapon import * 
from codloadouts.models.weapon_loadout import *

a = Attachment(attachment_type=AttachmentType.OPTIC, attachment_name='scout')
a2 = Attachment(attachment_type=AttachmentType.MUZZLE, attachment_name='compensator')
w = Weapon(weapon_type=WeaponType.PRIMARY, weapon_name='scar')
wl = WeaponLoadout(weapon_loadout_name='warzone', weapon=w, attachment_1=a, attachment_2=a2)
with app.app_context():
    db.drop_all()
    db.create_all() 

    db.session.add(a)
    db.session.add(a2)
    db.session.add(w)
    db.session.add(wl)

    db.session.commit()

    print(Weapon.query.all())
    print(Attachment.query.all())
    print(WeaponLoadout.query.all())


