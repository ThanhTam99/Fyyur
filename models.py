# models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Artists(db.Model):
    __tablename__ = 'artists'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    genre = db.Column(db.String(50))
    website = db.Column(db.String(120))
    bio = db.Column(db.Text)
    # Thêm các trường dữ liệu mới cho Artists

    shows = db.relationship('Shows', backref='artist', lazy=True)

class Venues(db.Model):
    __tablename__ = 'venues'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    city = db.Column(db.String(100))
    address = db.Column(db.String(200))
    capacity = db.Column(db.Integer)
    # Thêm các trường dữ liệu mới cho Venues

    shows = db.relationship('Shows', backref='venue', lazy=True)

class Shows(db.Model):
    __tablename__ = 'shows'

    id = db.Column(db.Integer, primary_key=True)
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'), nullable=False)
    venue_id = db.Column(db.Integer, db.ForeignKey('venues.id'), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime)
    ticket_price = db.Column(db.Float)
    # Thêm các trường dữ liệu mới cho Shows
