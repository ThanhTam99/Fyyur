# Fyyur
project-root
│
├── app.py # Khởi tạo Flask app và các config cơ bản
├── config.py # Cấu hình ứng dụng (Database URLs, CSRF, etc.)
├── models.py # Định nghĩa các SQLAlchemy models
├── forms.py # Định nghĩa các Flask-WTF forms (nếu có)
├── routes.py # Định nghĩa các routes cho ứng dụng
│
├── requirements.txt # Các thư viện cần thiết
├── README.md
├── error.log
│
├── static/
│   ├── css/
│   ├── font/
│   ├── ico/
│   ├── img/
│   └── js/
│
└── templates/
    ├── errors/
    ├── forms/
    ├── layouts/
    └── pages/

<link rel="stylesheet" href="{{ url_for('static', filename='css/bootstrap.min.css') }}">
<script src="{{ url_for('static', filename='js/bootstrap.min.js') }}"></script>