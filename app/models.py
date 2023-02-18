from app import db

class GetInfo(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    phone = db.Column(db.String(256))
    email = db.Column(db.String(256))
    text = db.Column(db.String(256))

    def __init__(self, name, phone, email, text):
        self.name = name
        self.phone = phone
        self.email = email
        self.text = text


class CreateWidget(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name_project = db.Column(db.String(256))
    url = db.Column(db.String(256))
    text = db.Column(db.String(256))
    number = db.Column(db.String(256))
    mono = db.Column(db.Integer)
    privat = db.Column(db.Integer)

    def __init__(self, name_project, url, text, number, mono, privat):
        self.name_project = name_project
        self.url = url
        self.text = text
        self.number = number
        self.mono = mono
        self.privat = privat
