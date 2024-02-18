# reminder.py

from datetime import datetime, timedelta

def display_reminders(events):
    now = datetime.now()
    next_hour = now + timedelta(hours=1)

    upcoming_events = [event for event in events if event.start_time > now and event.start_time < next_hour]
    if upcoming_events:
        print("Upcoming Events:")
        for event in upcoming_events:
            print(event)
    else:
        print("No upcoming events within the next hour.")
