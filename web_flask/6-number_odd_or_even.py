#!/usr/bin/python3
""" Script that starts a Flask web application """

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    return 'C ' + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythoniscool(text='is cool'):
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def nisanumber(n):
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def numbertemplate(n):
    return render_template('5-number.html', n=n)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def oddoreven(n):
    """ Displays a HTML page only if n is an integer """
    if n % 2 == 0:
        euen = 'even'
    else:
        euen = 'odd'
    return render_template('6-number_odd_or_even.html', n=n,
                           euen=euen)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')