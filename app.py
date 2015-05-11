from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/go_and_be')
def go_and_be():
    return render_template(\
        'go_and_be/index.html', \
        title='Go & Be', \
        active= 'go_and_be')

@app.route('/preschool')
def preschool():
    return render_template(\
        'preschool/index.html', \
        title='Preschool', \
        active= 'preschool')

@app.route('/adult_day_services')
def adult_day_services():
    return render_template(\
        'adult_day_services/index.html', \
        title='Adult Day Services', \
        active='adult_day_services')

@app.route('/youth')
def youth():
    return render_template(\
        'youth/index.html', \
        title='Youth Ministry', \
        active='youth')

@app.route('/discipleship')
def discipleship():
    return render_template(\
        'discipleship/index.html', \
        title='Discipleship', \
        active='discipleship')

@app.route('/media')
def media():
    return render_template(\
        'media/index.html', \
        title='Media', \
        active='media')

@app.route('/calendar')
def calendar():
    return render_template(\
        'calendar/index.html', \
        title='Calendar',
        active='calendar')

@app.route('/about')
def about():
    return render_template(\
        'about/index.html', \
        title='About', \
        active='about')

if __name__ == '__main__':
    debug = False
    try:
        debug = os.environ['DEBUG'] or False
    except KeyError:
        debug = False

    app.run(debug=debug)

