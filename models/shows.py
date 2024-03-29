from . import db

class Shows(db.Model):
    __tablename__ = 'shows'

    id = db.Column(db.Integer, primary_key=True)
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id', ondelete='CASCADE'), nullable=False)
    venue_id = db.Column(db.Integer, db.ForeignKey('venues.id', ondelete='CASCADE'), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime)
    ticket_price = db.Column(db.Float)
    # Thêm các trường dữ liệu mới cho Shows
