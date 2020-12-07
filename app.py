from flask import Flask, render_template

from data import title, subtitle, description, departures, tours


app = Flask(__name__)


@app.route('/test/')
def render_test():
    return render_template('about.html', test_dict={'name': 'test_dict_name'})


@app.route('/')
def render_main():
    return render_template('index.html',
                           title=title,
                           subtitle=subtitle,
                           description=description,
                           departures=departures,
                           tours=tours)


@app.route('/departures/<departure>/')
def render_departure(departure):
    departure_tours = {}
    price_list = []
    nights_list = []
    for key, tour in tours.items():
        if tour['departure'] == departure:
            departure_tours[key] = tour
            price_list.append(tour['price'])
            nights_list.append(tour['nights'])
    return render_template('departure.html',
                           title=title,
                           tours=departure_tours,
                           price_list=price_list,
                           nights_list=nights_list,
                           departures=departures,
                           departure=departure)


@app.route('/tours/<int:id>/')
def render_tour(id):
    tour_data = tours[id]
    tour_departure = departures[tour_data["departure"]]
    tour_stars = int(tour_data["stars"])
    return render_template('tour.html',
                           title=title,
                           tour=tour_data,
                           stars=tour_stars,
                           departure=tour_departure,
                           departures=departures)


#app.run('0.0.0.0', 8000)    #debag run


if __name__ == '__main__':   #production run
    app.run()