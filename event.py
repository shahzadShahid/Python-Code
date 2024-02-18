# event.py

class Event:
    def __init__(self, title, description, start_time, end_time):
        self.title = title
        self.description = description
        self.start_time = start_time
        self.end_time = end_time

    def __str__(self):
        return f"{self.title} ({self.start_time} to {self.end_time})"

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "start_time": self.start_time,
            "end_time": self.end_time
        }

    @classmethod
    def from_dict(cls, event_dict):
        return cls(event_dict["title"], event_dict["description"], event_dict["start_time"], event_dict["end_time"])
