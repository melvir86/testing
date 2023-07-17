import pytest
import sqlite3
import warnings
import json
import requests

def test_getAllUsers():
    # Prepare a JSON payload for the request
    payload = {
    }


    # Send a POST request to the backend endpoint with the payload
    response = requests.get('http://localhost:8085/api/v1/Users')

    # Check that the response status code is 200 (OK)
    assert response.status_code == 200
   
    
    # Check that user patient1 can be retrieved from the database
    users = response.json()
    print(users)

    assert users is not None
    assert users[0]["username"] == 'patient1'
    assert users[0]["password"] == 'Password123'
    assert users[0]["role"] == 'patient'
    
def test_loginUser():
    # Prepare a JSON payload for the request
    payload = {
    }

    #Request Parameters required to be passed to the backend are Username, Password and Role
    # Send a POST request to the backend endpoint with the payload
    response = requests.get('http://localhost:8085/api/v1/Users/login?username=patient1&password=Password123&role=patient', json = payload)

    # Check that the response status code is 200 (OK)
    assert response.status_code == 200
   
    
    # Check that user patient1 can be retrieved from the database
    users = response.json()
    print(users)

    assert users is not None
    assert users[0]["username"] == 'patient1'
    assert users[0]["password"] == 'Password123'
    assert users[0]["role"] == 'patient'