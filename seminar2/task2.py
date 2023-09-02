from flask import Flask, render_template, request, make_response


app = Flask(__name__)

# Задание №9
# 📌 Создать страницу, на которой будет форма для ввода имени
# и электронной почты
# 📌 При отправке которой будет создан cookie файл с данными
# пользователя
# 📌 Также будет произведено перенаправление на страницу
# приветствия, где будет отображаться имя пользователя.
# 📌 На странице приветствия должна быть кнопка "Выйти"
# 📌 При нажатии на кнопку будет удален cookie файл с данными
# пользователя и произведено перенаправление на страницу
# ввода имени и электронной почты.



@app.route('/email/', methods=['GET', 'POST'])
def email():
    if request.method == 'POST':
        response = make_response("Cookies установлены")
        name = request.form.get('name')
        email = request.form.get('email')
        content = {'name': name }
        response.set_cookie('name', name)
        response.set_cookie('email', email)
        return render_template('hello_name_log.html', **content)
    return render_template('email.html')  

@app.route('/logout/', methods=['GET', 'POST'])
def logout(): 
    if request.method == 'POST':
        response = make_response(render_template('email.html'))
        response.delete_cookie('name')
        response.delete_cookie('email')
        return response
    return render_template('email.html')
    

if __name__ == '__main__':
    app.run(debug=True)
