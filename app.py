from flask import Flask, render_template, request, redirect, url_for
from config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS
from models import db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS

# Đăng ký ứng dụng Flask với SQLAlchemy instance
db.init_app(app)

# Các routes của ứng dụng Flask
@app.route('/')
def index():
    users = User.query.all()
    return render_template('pages/index.html', users=users)

@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        new_user = User(username=username, email=email)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('pages/add_user.html')

@app.route('/update_user/<int:id>', methods=['GET', 'POST'])
def update_user(id):
    user = User.query.get_or_404(id)
    if request.method == 'POST':
        user.username = request.form['username']
        user.email = request.form['email']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('pages/update_user.html', user=user)

@app.route('/delete_user/<int:id>', methods=['GET', 'POST'])
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    # Tạo bảng users nếu chưa tồn tại
    with app.app_context():
        db.create_all()
    app.run(debug=True)
