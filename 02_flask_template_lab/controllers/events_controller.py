from flask import render_template, Blueprint, request
from models.event_list import events, add_new_event
from models.event import Event

events_blueprint = Blueprint("events", __name__)

@events_blueprint.route('/events')
def index():
    return render_template('index.jinja', title='The Event list', events=events)

@events_blueprint.route("/events", methods=["POST"])
def add_event():
    print(request.form)
    date = request.form["date"]
    name = request.form["name"]
    description = request.form["description"]
    number_of_guests = request.form["number of guests"]
    room_location = request.form["room location"] 
    new_event = Event(date, name, number_of_guests, room_location, description)
    add_new_event(new_event)
    return "Done"