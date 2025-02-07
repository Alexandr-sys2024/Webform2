from flask import render_template, request, redirect, url_for, flash
from app import app

# Переменная для хранения данных анкеты
user_data = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Получаем данные из формы
        name = request.form.get("name").strip()
        city = request.form.get("city").strip()
        hobby = request.form.get("hobby").strip()
        age = request.form.get("age").strip()

        # Проверяем, что все поля заполнены и возраст — число
        if not name or not city or not hobby or not age:
            flash("Все поля должны быть заполнены!", "danger")
        elif not age.isdigit() or int(age) <= 0:
            flash("Возраст должен быть положительным числом!", "warning")
        else:
            # Сохраняем данные анкеты в список
            user_data.append({
                "name": name,
                "city": city,
                "hobby": hobby,
                "age": int(age)
            })
            flash("Анкета успешно отправлена!", "success")
            return redirect(url_for("index"))
    
    return render_template("blog.html", user_data=user_data)
