#!/usr/bin/python3
"""
starts a Flask web application
"""

from models import storage
from models.state import State
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    return render_template("7-states_list.html", states=sorted(storage.all(State).values(), key=lambda x: x.name))


@app.teardown_appcontext
def teardown_appcontext(exception):
    storage.close()


if __name__ == "__main__":
    """returns Hello HBNB!"""
    app.run(host='0.0.0.0', port=5000)
