import pytest
import sqlite3
import warnings
import json
import requests

def test_getAllAppointments():
    # Prepare a JSON payload for the request
    payload = {
    }

    # Send a GET request to the backend endpoint with the payload
    response = requests.get('http://localhost:8084/api/v1/Appointments')

    # Check that the response status code is 200 (OK)
    assert response.status_code == 200
   
    
    # Check that the sample appointment info can be retrieved from the database
    appointments = response.json()
    print(appointments)

    assert appointments is not None
    assert appointments[0]["gp"] == 'The Civic Medical Centre'
    assert appointments[0]["appointment_type"] == 'New Health Problem'
    assert appointments[0]["user"] == 'patient1'
    
def test_getAppointment():
    # Prepare a JSON payload for the request
    payload = {
    }
   
    # Send a GET request to the backend endpoint with appointment's Id to retrieve information regarding that appointment
    response = requests.get('http://localhost:8084/api/v1/Appointments/64a7c981e1fb525690ac26fb', json = payload)

    # Check that the response status code is 200 (OK)
    assert response.status_code == 200
      
    # Check that the sample appointment info can be retrieved from the database
    appointments = response.json()
    print(appointments)

    assert appointments is not None
    assert appointments[0]["gp"] == 'The Civic Medical Centre'
    assert appointments[0]["appointment_type"] == 'New Health Problem'
    assert appointments[0]["user"] == 'patient1'
    
def test_getAppointmentsByUser():
    # Prepare a JSON payload for the request
    payload = {
    }
   
    # Send a GET request to the backend endpoint with patient1 parameter to retrieve all his Appointments
    response = requests.get('http://localhost:8084/api/v1/Appointments/user?user=patient1', json = payload)

    # Check that the response status code is 200 (OK)
    assert response.status_code == 200
   
    # Check that the sample appointment info can be retrieved from the database
    appointments = response.json()
    print(appointments)

    assert appointments is not None
    assert appointments[0]["gp"] == 'The Civic Medical Centre'
    assert appointments[0]["appointment_type"] == 'New Health Problem'
    assert appointments[0]["user"] == 'patient1'
    
def test_getAppointmentsByGPs():
    # Prepare a JSON payload for the request
    payload = {
    }
   
    # Send a GET request to the backend endpoint with The Civic Medical Centre parameter to retrieve all Appointments of their GP
    response = requests.get('http://localhost:8084/api/v1/Appointments/gp?gp=The Civic Medical Centre', json = payload)

    # Check that the response status code is 200 (OK)
    assert response.status_code == 200
   
    # Check that the sample appointment info can be retrieved from the database
    appointments = response.json()
    print(appointments)

    assert appointments is not None
    assert appointments[0]["gp"] == 'The Civic Medical Centre'
    assert appointments[0]["appointment_type"] == 'New Health Problem'
    assert appointments[0]["user"] == 'patient1'
    
def test_updateAppointmentInformation():
    # Prepare a JSON payload for the request
    payload = {
      "gp": "The Civic Medical Centre",
      "appointment_type": "New Health Problem",
      "appointment_symptom": "Have been having fever and flu the last 3 days.",
      "appointment_cause": "Over-exercising over the summer break.",
      "appointment_worry": "",
      "appointment_duration": "3 days",
      "appointment_symptomstatus": "Same",
      "appointment_improvement": "Tried paracetamol but it has not helped/",
      "appointment_doctor": "",
      "appointment_datetime": "2023-07-10T10:10",
      "consent_contact": "yes",
      "consent_sms": "yes",
      "consent_email": "yes",
      "user": "patient1",
      "status": "Submitted",
      "gp_comments": "Will schedule.",
    }

    # Send a PUT request to the backend endpoint to update Registration information with payload based on that Registrations ID which is 64a7c8005ef28c7f24a09325
    response = requests.put('http://localhost:8084/api/v1/Appointments/64a7c981e1fb525690ac26fb/', json = payload)

    # Check that the response status code is 200 (OK)
    assert response.status_code == 200
   
    appointments = response.json()
    print(appointments)
    
def test_createNewRegistration():
    # Prepare a JSON payload for the request
    payload = {
      "gp": "The Civic Medical Centre",
      "appointment_type": "New Health Problem",
      "appointment_symptom": "Diarrhea over the last day",
      "appointment_cause": "Ate the wrong food",
      "appointment_worry": "",
      "appointment_duration": "1 day",
      "appointment_symptomstatus": "Worse",
      "appointment_improvement": "Tried ultracarbon but it only worked temporarily",
      "appointment_doctor": "",
      "appointment_datetime": "",
      "consent_contact": "yes",
      "consent_sms": "yes",
      "consent_email": "yes",
      "user": "patient2",
      "status": "Submitted",
      "gp_comments": "",
    }

    # Send a POST request to the backend endpoint to update Registration information with payload based on that Registrations ID which is 64a7c8005ef28c7f24a09325
    response = requests.post('http://localhost:8084/api/v1/Appointments/', json = payload)

    # Check that the response status code is 200 (OK)
    assert response.status_code == 201
   
    appointments = response.json()
    print(appointments)