import pytest
import sqlite3
import warnings
import json
import requests

def test_getAllGPs():
    # Prepare a JSON payload for the request
    payload = {
    }

    # Send a GET request to the backend endpoint with the payload
    response = requests.get('http://localhost:8081/api/v1/GPs')

    # Check that the response status code is 200 (OK)
    assert response.status_code == 200
   
    
    # Check that user patient1 can be retrieved from the database
    gps = response.json()
    print(gps)

    assert gps is not None
    assert gps[0]["name"] == 'St Peters Medical Centre'
    assert gps[0]["borough"] == 'Harrow'
    assert gps[0]["status"] == 'Active'
    
def test_getGPByAdmin():
    # Prepare a JSON payload for the request
    payload = {
    }
   
    # Send a GET request to the backend endpoint with gpadmin1 parameter to retrieve GP information related to his user
    response = requests.get('http://localhost:8081/api/v1/GPs/gpadmin1', json = payload)

    # Check that the response status code is 200 (OK)
    assert response.status_code == 200
   
    
    # Check that gp information can be retrieved from the database
    gps = response.json()
    print(gps)

    assert gps is not None
    assert gps[0]["name"] == 'St Peters Medical Centre'
    assert gps[0]["borough"] == 'Harrow'
    assert gps[0]["status"] == 'Active'
    
def test_getGPByName():
    # Prepare a JSON payload for the request
    payload = {
    }
   
    # Send a GET request to the backend endpoint with gpadmin1 parameter to retrieve GP information based on name passed in
    response = requests.get('http://localhost:8081/api/v1/GPs/name/St Peters Medical Centre', json = payload)

    # Check that the response status code is 200 (OK)
    assert response.status_code == 200
   
    
    # Check that gp information can be retrieved from the database
    gps = response.json()
    print(gps)

    assert gps is not None
    assert gps[0]["name"] == 'St Peters Medical Centre'
    assert gps[0]["borough"] == 'Harrow'
    assert gps[0]["status"] == 'Active'
    
def test_getGPByBorough():
    # Prepare a JSON payload for the request
    payload = {
    }
  
    # Send a GET request to the backend endpoint with Harrow parameter to retrieve GP information based on borough passed in
    response = requests.get('http://localhost:8081/api/v1/GPs/borough/Harrow', json = payload)

    # Check that the response status code is 200 (OK)
    assert response.status_code == 200
   
    
    # Check that gp information can be retrieved from the database
    gps = response.json()
    print(gps)

    assert gps is not None
    assert gps[0]["name"] == 'St Peters Medical Centre'
    assert gps[0]["borough"] == 'Harrow'
    assert gps[0]["status"] == 'Active'
    
def test_getGPByLeastCurrentCapacityByBorough():
    # Prepare a JSON payload for the request
    payload = {
    }
  
    # Send a GET request to the backend endpoint with Harrow and selected PrimaryGP to retrieve secondary GP by system based on least current capacity
    response = requests.get('http://localhost:8081/api/v1/GPs/borough/recommended/Harrow?primaryGP=St Peters Medical Centre', json = payload)

    # Check that the response status code is 200 (OK)
    assert response.status_code == 200
   
    
    # Check that gp information can be retrieved from the database
    gps = response.json()
    print(gps)

    assert gps is not None
    assert gps[0]["name"] == 'Savita Medical Centre Dr Muhammad Shahzad'
    assert gps[0]["borough"] == 'Harrow'
    assert gps[0]["status"] == 'Active'
    
def test_updateGPInformation():
    # Prepare a JSON payload for the request
    payload = {
    "name": "St Peters Medical Centre",
    "address": "1 Colbeck Rd, Harrow HA1 4BS - Latest Updated Address",
    "borough": "Harrow",
    "telephone": "0208 864 4868",
    "maxcapacity": 500,
    "currentcapacity": 10,
    "status": "Active",
    "admin": "gpadmin1",
    }
  
    # Send a PUT request to the backend endpoint to update GP information with payload based on that GPs ID which is 64528d6f7a461d7b1a14f92b
    response = requests.put('http://localhost:8081/api/v1/GPs/64528d6f7a461d7b1a14f92b/', json = payload)

    # Check that the response status code is 200 (OK)
    assert response.status_code == 200
   
    gps = response.json()
    print(gps)