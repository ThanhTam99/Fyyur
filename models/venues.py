from . import db

class Venues(db.Model):
    __tablename__ = 'venues'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    city = db.Column(db.String(100))
    address = db.Column(db.String(200))
    capacity = db.Column(db.Integer)
    # Thêm các trường dữ liệu mới cho Venues
