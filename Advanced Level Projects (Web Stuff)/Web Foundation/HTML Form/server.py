from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.form['username'] == 'Kaushal' and request.form['password'] == '12345678':
        return render_template('login.html', name=request.form['username'], password=request.form['password'])
    else:
        return render_template('notlogin.html')


if __name__ == '__main__':
    app.run(debug=True)
