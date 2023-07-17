import pytest
import sqlite3
import warnings
import json
import requests

def test_getAllRegistrations():
    # Prepare a JSON payload for the request
    payload = {
    }

    # Send a GET request to the backend endpoint with the payload
    response = requests.get('http://localhost:8082/api/v1/Registrations')

    # Check that the response status code is 200 (OK)
    assert response.status_code == 200
   
    
    # Check that the sample registration info can be retrieved from the database
    registrations = response.json()
    print(registrations)

    assert registrations is not None
    assert registrations[0]["basic_forename"] == 'Melvir'
    assert registrations[0]["basic_surname"] == 'Singh Sidhu'
    assert registrations[0]["basic_height"] == '170'
    
def test_getRegistration():
    # Prepare a JSON payload for the request
    payload = {
    }
   
    # Send a GET request to the backend endpoint with registration's Id to retrieve information regarding that registration
    response = requests.get('http://localhost:8082/api/v1/Registrations/64a7c8005ef28c7f24a09325', json = payload)

    # Check that the response status code is 200 (OK)
    assert response.status_code == 200
   
    
    # Check that the sample registration info can be retrieved from the database
    registrations = response.json()
    print(registrations)

    assert registrations is not None
    assert registrations[0]["basic_forename"] == 'Melvir'
    assert registrations[0]["basic_surname"] == 'Singh Sidhu'
    assert registrations[0]["basic_height"] == '170'
    
def test_getRegistrationByUser():
    # Prepare a JSON payload for the request
    payload = {
    }
   
    # Send a GET request to the backend endpoint with patient1 parameter to retrieve all his Registrations
    response = requests.get('http://localhost:8082/api/v1/Registrations/user?user=patient1', json = payload)

    # Check that the response status code is 200 (OK)
    assert response.status_code == 200
   
    # Check that the sample registration info can be retrieved from the database
    registrations = response.json()
    print(registrations)

    assert registrations is not None
    assert registrations[0]["basic_forename"] == 'Melvir'
    assert registrations[0]["basic_surname"] == 'Singh Sidhu'
    assert registrations[0]["basic_height"] == '170'
    
def test_getRegistrationByGPs():
    # Prepare a JSON payload for the request
    payload = {
    }
   
    # Send a GET request to the backend endpoint with The Civic Medical Centre parameter to retrieve all Registrations to their GP
    response = requests.get('http://localhost:8082/api/v1/Registrations/gp_primary?gp_primary=The Civic Medical Centre', json = payload)

    # Check that the response status code is 200 (OK)
    assert response.status_code == 200
   
    # Check that the sample registration info can be retrieved from the database
    registrations = response.json()
    print(registrations)

    assert registrations is not None
    assert registrations[0]["basic_forename"] == 'Melvir'
    assert registrations[0]["basic_surname"] == 'Singh Sidhu'
    assert registrations[0]["basic_height"] == '170'
    
def test_updateRegistrationInformation():
    # Prepare a JSON payload for the request
    payload = {
      "basic_forename": "Melvir",
      "basic_surname": "Singh Sidhu",
      "basic_dob": "1986-07-14",
      "basic_height": "170",
      "basic_weight": "65",
      "basic_nhsnumber": "",
      "basic_country": "United Kingdom",
      "basic_gender": "male",
      "basic_address": "FLAT 5\n81 HINDES ROAD",
      "basic_postcode": "HA11SQ",
      "basic_email": "simplyuntitled86@hotmail.com",
      "health_suffered": "NA",
      "health_suffereddetails": "",
      "health_operations": "no",
      "health_TB": "no",
      "health_TBCountry": "no",
      "health_smoke": "no",
      "health_drink": "yes",
      "health_disability": "no",
      "health_disabilitydetails": "",
      "health_allergy": "no",
      "health_allergydetails": "",
      "health_medication": "no",
      "health_medicationdetails": "",
      "health_exercise": "threetimesormore",
      "family_illnesss": "hpn",
      "family_illnesssdetails": "Dad suffers from HBP. Has suffered from it for the last 3 years but is under control with medication. I do not have HPB.",
      "family_carer": "no",
      "family_carerdetails": "",
      "profiling_englishspoken": "no",
      "profiling_englishwritten": "no",
      "profiling_englishfirst": "yes",
      "profiling_religion": "noanswer",
      "profiling_ethnicgroup": "asian",
      "gp_borough": "Harrow",
      "gpprimary": "The Civic Medical Centre",
      "gp_secondary": "Savita Medical Centre Dr Muhammad Shahzad",
      "consent_resident": "yes",
      "consent_eea": "no",
      "consent_prc": "no",
      "consent_sms": "yes",
      "consent_email": "yes",
      "user": "patient1",
      "status": "Registered",
    }

    # Send a PUT request to the backend endpoint to update Registration information with payload based on that Registrations ID which is 64a7c8005ef28c7f24a09325
    response = requests.put('http://localhost:8082/api/v1/Registrations/64a7c8005ef28c7f24a09325/', json = payload)

    # Check that the response status code is 200 (OK)
    assert response.status_code == 200
   
    registrations = response.json()
    print(registrations)
    
def test_createNewRegistration():
    # Prepare a JSON payload for the request
    payload = {
      "basic_forename": "John",
      "basic_surname": "Doe",
      "basic_dob": "1986-07-14",
      "basic_height": "170",
      "basic_weight": "65",
      "basic_nhsnumber": "",
      "basic_country": "United Kingdom",
      "basic_gender": "male",
      "basic_address": "FLAT 5\n81 HINDES ROAD",
      "basic_postcode": "HA11SQ",
      "basic_email": "simplyuntitled86@hotmail.com",
      "health_suffered": "NA",
      "health_suffereddetails": "",
      "health_operations": "no",
      "health_TB": "no",
      "health_TBCountry": "no",
      "health_smoke": "no",
      "health_drink": "yes",
      "health_disability": "no",
      "health_disabilitydetails": "",
      "health_allergy": "no",
      "health_allergydetails": "",
      "health_medication": "no",
      "health_medicationdetails": "",
      "health_exercise": "threetimesormore",
      "family_illnesss": "hpn",
      "family_illnesssdetails": "",
      "family_carer": "no",
      "family_carerdetails": "",
      "profiling_englishspoken": "no",
      "profiling_englishwritten": "no",
      "profiling_englishfirst": "yes",
      "profiling_religion": "noanswer",
      "profiling_ethnicgroup": "asian",
      "gp_borough": "Harrow",
      "gpprimary": "The Civic Medical Centre",
      "gp_secondary": "Savita Medical Centre Dr Muhammad Shahzad",
      "consent_resident": "yes",
      "consent_eea": "no",
      "consent_prc": "no",
      "consent_sms": "yes",
      "consent_email": "yes",
      "user": "patient2",
      "status": "Registered",
    }

    # Send a POST request to the backend endpoint to update Registration information with payload based on that Registrations ID which is 64a7c8005ef28c7f24a09325
    response = requests.post('http://localhost:8082/api/v1/Registrations/', json = payload)

    # Check that the response status code is 200 (OK)
    assert response.status_code == 201
   
    registrations = response.json()
    print(registrations)