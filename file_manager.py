# file_manager.py

import json

def save_events_to_file(events, filename):
    with open(filename, 'w') as file:
        json.dump([event.to_dict() for event in events], file)

def load_events_from_file(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            return [Event.from_dict(event_dict) for event_dict in data]
    except FileNotFoundError:
        return []
