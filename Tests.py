# importing the requests library
import requests
import pytest
import json

##############################################################################
# Sensors data table functionality test
##############################################################################

#GET

def test_get_city_returns_correct_status():
    URL_sensor = "http://127.0.0.1:5000/sensor"
    PARAMS_sensor = {'city':'Washington'}
    r = requests.get(url = URL_sensor, params = PARAMS_sensor)
    print(r.json())
    assert r.status_code == 200

def test_get_city_returns_correct_length():
    URL_sensor = "http://127.0.0.1:5000/sensor"
    PARAMS_sensor = {'city':'Washington'}
    r = requests.get(url = URL_sensor, params = PARAMS_sensor)
    data = r.json()
    assert len(data) == 11
    
#POST    

def test_post_city_returns_correct_status():
    URL_sensor = "http://127.0.0.1:5000/sensor"
    r = requests.post(url = URL_sensor, json = {'city':'Dubai','country':'UAE'})
    print(r)
    data = r.json()
    print(data)
    assert r.status_code == 201

def test_post_city_returns_correct_length():
    URL_sensor = "http://127.0.0.1:5000/sensor"
    r = requests.post(url = URL_sensor, json = {'city':'Dubai','country':'UAE'})
    data = r.json()
    assert len(data) == 2

##############################################################################
# Sensor data table functionality test
##############################################################################


#GET

def test_get_data_returns_correct_status():
    URL_sensor = "http://127.0.0.1:5000/sensordata"
    PARAMS_sensor = {'ID':json.dumps([1,2,10]),'start':1,'end':1742978037881}
    r = requests.get(url = URL_sensor, params = PARAMS_sensor)
    assert r.status_code == 200

def test_get_data_returns_correct_length():
    URL_sensor = "http://127.0.0.1:5000/sensordata"
    PARAMS_sensor = {'ID':json.dumps([1,2,10]),'start':1,'end':1742978037881}
    r = requests.get(url = URL_sensor, params = PARAMS_sensor)
    data = r.json()
    assert len(data) == 2
    
#POST    

def test_post_data_returns_correct_status():
    URL_sensor = "http://127.0.0.1:5000/sensordata"
    r = requests.post(url = URL_sensor, json = {'ID':1,'humidity':10.9,'temperature':12.4})
    assert r.status_code == 201

def test_post_data_returns_correct_length():
    URL_sensor = "http://127.0.0.1:5000/sensordata"
    r = requests.post(url = URL_sensor, json = {'ID':1,'humidity':10.9,'temperature':12.4})
    data = r.json()
    assert len(data) == 3

