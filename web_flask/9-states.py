#!/usr/bin/python3
"""
starts a Flask web application
"""

from models import storage
from models.state import State
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/states", strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def state(id=None):
    states = storage.all(State).values()
    my_state = None
    if id is not None:
        for state in states:
            if state.id == id:
                my_state = state
    return render_template("9-states.html", states=states,
                           state=my_state, id=id)


@app.teardown_appcontext
def teardown(exception):
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
