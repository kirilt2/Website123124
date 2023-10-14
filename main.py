from flask import Flask, request, render_template

app = Flask(__name__, template_folder="C:/Users/kiril/Code/pythonProject1/templates")

# Create a list to store orders
orders = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nickname = request.form.get('nickname')
        donate = request.form.get('donate')
        cheat_clients = request.form.get('cheat-clients')
        cheat_duration = request.form.get('cheat-duration')
        play_hours = request.form.get('play-hours')
        age = request.form.get('age')

        if not (nickname and donate and cheat_clients and cheat_duration and play_hours and age):
            return "Отправка формы не удалась. Пожалуйста, заполните все поля."

        data = {
            'nickname': nickname,
            'donate': donate,
            'cheat-clients': cheat_clients,
            'cheat-duration': cheat_duration,
            'play-hours': play_hours,
            'age': age
        }
        orders.append(data)
        return render_template('send.html')
    return render_template('index.html')

@app.route('/orders')
def view_orders():
    print(orders)
    return render_template('orders.html', orders=orders)


if __name__ == '__main__':
    app.run(debug=True)
