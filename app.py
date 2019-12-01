from flask_sqlalchemy import SQLAlchemy
import os
from flask import Flask, request, jsonify, Response
import json
import states_data_source

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import State


@app.route("/state", methods=['GET'])
def get_last():
    try:
        state = State.query.order_by(State.timestamp.desc()).first()
        new_state = states_data_source.get_error(state)
        return jsonify(new_state)
    except Exception as e:
        return (str(e))


@app.route('/add_state', methods=['POST'])
def add_state():
    if request.method == 'POST':
        state = State(
            tp=request.form['tp'],
            tc=request.form['tc'],
            T=request.form['T'],
            b=request.form['b'],
            h=request.form['h'],
            timestamp=request.form['timestamp']
        )

        try:

            db.session.add(state)
            db.session.commit()
        except Exception as e:
            return (str(e))

        return Response(json.dumps({'stop': states_data_source.should_stop}), status=201)

    else:
        return Response('Bed method', status=405)


@app.route('/stop', methods=['POST'])
def stop():
    if request.method == 'POST':
        states_data_source.set_should_stop(request.form['stop'])
        return Response('Should_stop was updated to {}'.format(states_data_source.should_stop), status=201)
    else:
        return Response('Bed method', status=405)


@app.route("/getall")
def get_all():
    try:
        states = State.query.all()
        return jsonify([e.serialize() for e in states])
    except Exception as e:
        return(str(e))


if __name__ == '__main__':
    app.run()

# source env/bin/activate
# python manage.py runserver
