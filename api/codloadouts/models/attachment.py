from codloadouts import db     

class Attachment(db.Model):

    __tablename__ = 'attachment'
    id = db.Column(db.Integer, primary_key=True)

    attachment_type = db.Column(db.Text, index=False, unique=False, nullable=False)

    attachment_name = db.Column(db.Text, index=False, unique=False, nullable=False)

    @property
    def serialize(self):
        return {
            'attachment_type': self.attachment_type,
            'attachment_name': self.attachment_name
            }

    def __repr__(self):
        return '<Attachment {}: {}>'.format(self.attachment_type, self.attachment_name)

