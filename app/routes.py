from flask import render_template, request, redirect, url_for
from app import app

# Переменная для хранения данных анкеты
user_data = []


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Получаем данные из формы
        name = request.form.get("name")
        city = request.form.get("city")
        hobby = request.form.get("hobby")
        age = request.form.get("age")

        # Сохраняем данные анкеты в список, если все поля заполнены
        if name and city and hobby and age:
            user_data.append({
                "name": name,
                "city": city,
                "hobby": hobby,
                "age": age
            })
            return redirect(url_for("index"))

    # Передаем данные анкеты в шаблон для отображения
    return render_template("blog.html", user_data=user_data)
