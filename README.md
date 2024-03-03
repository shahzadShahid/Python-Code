This README file includes instructions on how to run the application, dependencies, API endpoints, and usage examples

# Event Management System

## Introduction
This is a simple Python backend application built with Flask that allows users to manage events. Users can add, view, update, and delete events. Each event includes a title, description, start time, and end time.

## Requirements
- Python 3.x
- REST APIs
- Flask


## Installation
1. Clone the repository:
 	https://github.com/shahzadShahid/Python-Code.git
2. Navigate to the project directory:
	cd event-management
3. Install dependencies:
	pip install -r requirements.txt

## Usage
1. Start the Flask application:
	python app.py

2. The application will be running on `http://localhost:5000`.

## API Endpoints
- **POST /events**: Add a new event
- **GET /events**: View all events
- **PUT /events/<index>**: Update an existing event
- **DELETE /events/<index>**: Delete an event

## Usage Examples

### Adding an Event
- **Method**: POST
- **URL**: `http://localhost:5000/events`
- **Request Body**:
```json
{
   "title": "Meeting",
   "description": "Discuss project",
   "start_time": "2024-02-18T14:00:00",
   "end_time": "2024-02-18T15:00:00"
}
Response: 201 Created
Viewing All Events
Method: GET
URL: http://localhost:5000/events
Response: List of events in JSON format

### Updating an Event
Method: PUT
URL: http://localhost:5000/events/<index> (replace <index> with the index of the event)
Request Body:
{
    "title": "Updated Meeting",
    "description": "Discuss project updates",
    "start_time": "2024-02-18T15:00:00",
    "end_time": "2024-02-18T16:00:00"
}
Response: 200 OK

### Deleting an Event
Method: DELETE
URL: http://localhost:5000/events/<index> (replace <index> with the index of the event)
Response: 200 OK
