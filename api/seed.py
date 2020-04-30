from codloadouts import create_app   
from flask_sqlalchemy import SQLAlchemy

app = create_app()
db = SQLAlchemy(app)

from codloadouts.models.attachment import * 
from codloadouts.models.weapon import * 

a = Attachment(attachment_type=AttachmentType.OPTIC, attachment_name='scout')
w = Weapon(weapon_type=WeaponType.PRIMARY, weapon_name='scar')

with app.app_context():
    db.drop_all()
    db.create_all() 

    db.session.add(a)
    db.session.add(w)

    db.session.commit()

    print(Weapon.query.all())
    print(Attachment.query.all())


