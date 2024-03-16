# app.py
from flask import Flask
from models import db
from config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS
from routes import init_app  # Import hàm init_app từ file routes

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS

# Khởi tạo SQLAlchemy cho ứng dụng Flask
db.init_app(app)

# Đăng ký các route từ file routes
init_app(app)

if __name__ == '__main__':
    app.run(debug=True)

