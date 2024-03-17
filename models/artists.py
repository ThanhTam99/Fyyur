from . import db

class Artists(db.Model):
    __tablename__ = 'artists'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    genre = db.Column(db.String(50))
    website = db.Column(db.String(120))
    bio = db.Column(db.Text)