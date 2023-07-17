import pytest
import sqlite3
import warnings
import json
import requests

def test_getAllFeedbacks():
    # Prepare a JSON payload for the request
    payload = {
    }

    # Send a GET request to the backend endpoint with the payload
    response = requests.get('http://localhost:8083/api/v1/feedbacks')

    # Check that the response status code is 200 (OK)
    assert response.status_code == 200
    
    # Check that the sample feedback info can be retrieved from the database
    feedbacks = response.json()
    print(feedbacks)

    assert feedbacks is not None
    assert feedbacks[0]["type"] == 'functionality'
    assert feedbacks[0]["status"] == 'Pending'
    assert feedbacks[0]["user"] == 'patient1'
    
def test_getFeedback():
    # Prepare a JSON payload for the request
    payload = {
    }
   
    # Send a GET request to the backend endpoint with feedback's Id to retrieve information regarding that feedback
    response = requests.get('http://localhost:8083/api/v1/feedbacks/64a7ca1951409b66ee287e97', json = payload)

    # Check that the response status code is 200 (OK)
    assert response.status_code == 200
      
    # Check that the sample feedback info can be retrieved from the database
    feedbacks = response.json()
    print(feedbacks)

    assert feedbacks is not None
    assert feedbacks[0]["type"] == 'functionality'
    assert feedbacks[0]["status"] == 'Pending'
    assert feedbacks[0]["user"] == 'patient1'
    
def test_getFeedbacksByUser():
    # Prepare a JSON payload for the request
    payload = {
    }
   
    # Send a GET request to the backend endpoint with patient1 parameter to retrieve all his Appointments
    response = requests.get('http://localhost:8083/api/v1/feedbacks/user?user=patient1', json = payload)

    # Check that the response status code is 200 (OK)
    assert response.status_code == 200
   
    # Check that the sample feedback info can be retrieved from the database
    feedbacks = response.json()
    print(feedbacks)

    assert feedbacks is not None
    assert feedbacks[0]["type"] == 'functionality'
    assert feedbacks[0]["status"] == 'Pending'
    assert feedbacks[0]["user"] == 'patient1'
    
def test_updateFeedbackInformation():
    # Prepare a JSON payload for the request
    payload = {
      "user": "patient1",
      "type": "functionality",
      "feedback": "I have updated my feedback from the testing code. Could you add in a live chat function to further improve real-time comms?",
      "status": "Pending",
    }

    # Send a PUT request to the backend endpoint to update Feedback information with payload based on that Feedback ID which is 64a7ca1951409b66ee287e97
    response = requests.put('http://localhost:8083/api/v1/feedbacks/64a7ca1951409b66ee287e97/', json = payload)

    # Check that the response status code is 200 (OK)
    assert response.status_code == 200
   
    feedbacks = response.json()
    print(feedbacks)
    
def test_createNewFeedback():
    # Prepare a JSON payload for the request
    payload = {
      "user": "patient2",
      "type": "functionality",
      "feedback": "I am creating a new entry from feedback from the testing code. Could you pls add in XXX functionality?",
      "status": "Pending",
    }

    # Send a POST request to the backend endpoint to update Registration information with payload based on that Registrations ID which is 64a7c8005ef28c7f24a09325
    response = requests.post('http://localhost:8083/api/v1/feedbacks/', json = payload)

    # Check that the response status code is 200 (OK)
    assert response.status_code == 201
   
    feedbacks = response.json()
    print(feedbacks)