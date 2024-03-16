from flask import Flask
from config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS
from models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS
db.init_app(app)
    
# Import các routes từ routes.py
from routes import *  # Thay vì import users, import tất cả các routes

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
