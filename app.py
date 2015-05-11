from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title="Bethel Lutheran Church & Preschool")

if __name__ == '__main__':
    debug = False
    try:
        debug = os.environ['DEBUG'] or False
    except KeyError:
        debug = False

    app.run(debug=debug)

