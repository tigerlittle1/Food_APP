from flask import Flask, render_template, request, redirect, url_for, send_from_directory, flash, send_file, make_response
from flask import jsonify

account = ["tes"]
password = ["test123"]

app = Flask(__name__)
app.secret_key = app.config.get('flask', 'secret_key')
app.config['UPLOAD_FOLDER'] = 'upload/'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        response = make_response(render_template("login.html"))
        response.headers['login_state'] = "False"
        response.headers['black'] = "False"
        return response

    if request.method == 'POST':
        user_account = request.form.get('user_account')
        user_password = request.form.get('user_password')
        print(user_account,user_password)

        for i in range(len(account)):
            if user_account == account[i] and user_password == password[i]:
                return "True"
            else:
                response = make_response(render_template("login.html"))
                response.headers['login_state'] = "False"
                response.headers['black'] = "False"
                return response

    # response = make_response(redirect(url_for('Data_base')))
    # response.headers['login_state'] = "True"


if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=int("8000"),
        debug=True,
    )
