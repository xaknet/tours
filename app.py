# -*- coding: utf-8 -*-
from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension
import data
from flask import request

app = Flask(__name__)

app.debug = True

app.config['SECRET_KEY'] = 'YTOIHWEFHGSI'


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/departure/<departure>')
def departure(departure):
    return render_template("departure.html")


@app.route('/tour/<id>')
def tour(id):
    return render_template("tour.html")


@app.errorhandler(404)
def not_found(e):
    return "Ничего не нашлось! Вот неудача, отправляйтесь на главную!"


@app.errorhandler(500)
def server_error(e):
    return "Что то не так, но мы все починим"


app.run()
toolbar = DebugToolbarExtension
