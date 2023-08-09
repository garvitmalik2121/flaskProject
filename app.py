""" prac 10 flask project"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return '<h1>Hello World :)</h1'


# @app.route('/greet')
# def greet():
#     return "Hello"
@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"


@app.route('/celsius_to_fahrenheit')
@app.route('/celsius_to_fahrenheit/<float:celsius>')
def celsius_to_fahrenheit(celsius=""):
    fahrenheit = convert_into_fahrenheit(celsius)
    return f"{celsius:.2f} C is {fahrenheit:.2f} F"


def convert_into_fahrenheit(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


if __name__ == '__main__':
    app.run()
