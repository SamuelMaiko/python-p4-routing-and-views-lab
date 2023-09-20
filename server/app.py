#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:my_string>')
def print_string(my_string):
    print(my_string)
    return my_string

@app.route('/count/<int:my_number>')
def count(my_number):
    numbers=range(1,my_number+1)
    result='\n'.join(map(str,numbers))
    return result

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1,operation,num2):
    if operation=="div":
        operation="/"
    result=eval(f'{num1}{operation}{num2}')
    return f'{result}'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
