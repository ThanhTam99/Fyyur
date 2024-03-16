from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class BaseUser(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<Artist %r>' % self.username

class Artists(BaseUser):
    __tablename__ = 'artists'

class Venues(BaseUser):
    __tablename__ = 'venues'
