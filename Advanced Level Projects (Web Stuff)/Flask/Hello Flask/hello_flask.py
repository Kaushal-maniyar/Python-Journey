from flask import Flask
app = Flask(__name__)


def make_h1(function):
    def wrapper_function():
        return f'<h1>{function()}</h1>'
    return wrapper_function


@app.route("/")
@make_h1
def hello() -> str:
    return "Hello World"


if __name__ == '__main__':
    app.run(debug=True)
