from event import Event
from file_manager import save_events_to_file, load_events_from_file


# event_manager.py

# event_manager.py

import json

class EventManager:
    def __init__(self):
        self.events = []

    def add_event(self, event):
        self.events.append(event)

    def update_event(self, index, updated_event):
        if 0 <= index < len(self.events):
            self.events[index] = updated_event
        else:
            raise IndexError("Event index is out of range")

    def delete_event(self, index):
        if 0 <= index < len(self.events):
            del self.events[index]
        else:
            raise IndexError("Event index is out of range")

    def get_sorted_events(self):
        return sorted(self.events, key=lambda x: x.start_time)

    def search_events(self, query):
        try:
            return [event for event in self.events if query in event.title or query in event.description]
        except Exception as e:
            raise Exception(f"Error occurred while searching events: {str(e)}")

    def load_events(self, filename):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                self.events = [Event.from_dict(event_dict) for event_dict in data]
        except FileNotFoundError:
            self.events = []

    def save_events(self, filename):
        with open(filename, 'w') as file:
            json.dump([event.to_dict() for event in self.events], file)
