from models.event import Event

event1 = Event("01.06.2021", "Joseph's Stagdo", 10, "Conference Room", "It's a fun stag do.")
event2 = Event("01.07.2021", "Green Festival", 2, "MotherEarth Room", "GrennPeace conference.")
event3 = Event("01.06.2021", "Wedding", 35, "Basement", "Begening of a beautiful relationship.")

events = [event1, event2, event3]

def add_new_event(event):
    events.append(event)
