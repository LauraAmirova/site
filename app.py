from flask import Flask, request, render_template

app = Flask(name)

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # Логика обработки обратной связи
        # Например, сохранение в базу данных или отправка по email
        print(f"Новое сообщение от {name} ({email}): {message}")

        return f"Спасибо за ваше сообщение, {name}!"

    # Отображение формы для метода GET
    return render_template('feedback.html')

if name == 'main':
    app.run(debug=True)
