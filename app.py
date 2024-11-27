from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def registration_form():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register_user():
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']

    with open('users.txt', 'a') as file:
        file.write(f'{username},{password},{email}\n')

    return f'<h1>Пользователь {username} успешно зарегистрирован!</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
