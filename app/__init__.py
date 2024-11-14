from flask import Flask

# Создаем экземпляр Flask-приложения
app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'

# Импортируем маршруты
from app import routes
