# -*- coding: utf-8 -*-
from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension
import data
from data import tours
from flask import request

app = Flask(__name__)


app.debug = True

app.config['SECRET_KEY'] = 'YTOIHWEFHGSI'


@app.route('/')
def main():
    limit_items = 6
    return render_template('index.html',
                           title=data.title,
                           description=data.description,
                           subtitle=data.subtitle,
                           departures=data.departures,
                           tours=data.tours,
                           limit_items=limit_items)


@app.route('/departure/<departure>')
def departure(departure):
    keys_list = []
    tours_list = []
    tours_dict = {}
    for key, value in tours.items():
        if departure == value.get("departure"):
            tours_list.append(value)
            tours_dict[key] = value
        else:
            print("Item not found")

    return render_template("departure.html",
                           departures=data.departures,
                           title=data.title,
                           departure=departure,
                           tours_list=tours_list,
                           keys_list=keys_list,
                           tours_dict=tours_dict,
                           tours=tours.items())


@app.route('/tour/<int:id>')
def tour(id):
    if id in tours.keys():
        id = tours.get(id)
    else:
        return not_found(404)

    current_country = id.get("departure")
    from_city = data.departures.get(current_country)


    output = render_template("tour.html",
                             id=id,
                             title=id.get("title"),
                             description=id.get("description"),
                             departure=id.get("departure"),
                             picture=id.get("picture"),
                             price=id.get("price"),
                             stars=int(id.get("stars")),
                             country=id.get("country"),
                             nights=id.get("nights"),
                             date=id.get("date"),
                             departures=data.departures,
                             current_country=current_country,
                             from_city=from_city,
                             )

    return output


@app.errorhandler(404)
def not_found(e):
    return "Ничего не нашлось! Вот неудача, отправляйтесь на главную!"


@app.errorhandler(500)
def server_error(e):
    return "Что то не так, но мы все починим"


if __name__ == '__main__':
    app.run()
toolbar = DebugToolbarExtension
