# app.py

from flask import Flask, jsonify, request
from event import Event
from event_manager import EventManager

app = Flask(__name__)
event_manager = EventManager()

@app.route('/events', methods=['POST'])
def add_event():
    try:
        data = request.get_json()
        event = Event(**data)
        event_manager.add_event(event)
        event_manager.save_events("events.json")
        return jsonify({"message": "Event added successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/events', methods=['GET'])
def get_events():
    try:
        event_manager.load_events("events.json")
        query = request.args.get('query')
        if query:
            events = event_manager.search_events(query)
        else:
            events = event_manager.get_sorted_events()
        return jsonify([event.to_dict() for event in events])
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/events/<int:index>', methods=['PUT'])
def update_event(index):
    try:
        data = request.get_json()
        updated_event = Event(**data)
        event_manager.update_event(index, updated_event)
        event_manager.save_events("events.json")
        return jsonify({"message": "Event updated successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/events/<int:index>', methods=['DELETE'])
def delete_event(index):
    try:
        event_manager.load_events("events.json")
        event_manager.delete_event(index)
        event_manager.save_events("events.json")
        return jsonify({"message": "Event deleted successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
    
@app.route('/events', methods=['GET'])
def get_search_events():
    try:
        event_manager.load_events("events.json")
        query = request.args.get('query')
        if query:
            events = event_manager.search_events(query)
        else:
            events = event_manager.get_sorted_events()
        return jsonify([event.to_dict() for event in events])
    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True)
