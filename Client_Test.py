# importing the requests library
import requests
import pytest 
import json
##############################################################################
# Sensor data table functionality test
##############################################################################
URL_sensor = "http://127.0.0.1:5000/sensor"
  
#GET

PARAMS_sensor = {'city':'Washington'}
r = requests.get(url = URL_sensor, params = PARAMS_sensor)
print(r)
data = r.json()
print(data)

#POST
  
r = requests.post(url = URL_sensor, json = {'city':'Dubai','country':'UAE'})
print(r)
data = r.json()
print(data)

##############################################################################
# Sensor data table functionality test
##############################################################################
URL_sensor = "http://127.0.0.1:5000/sensordata"

#GET

PARAMS_sensor = {'ID':json.dumps([1,2,10]),'start':1,'end':1742978037881}
print(PARAMS_sensor)
r = requests.get(url = URL_sensor, params = PARAMS_sensor)
print(r)
data = r.json()
print(data)

#POST
  
r = requests.post(url = URL_sensor, json = {'ID':10,'humidity':10.9,'temperature':12.4})
print(r)
data = r.json()
print(data)

#sensor ID 1000 doesnt exist
r = requests.post(url = URL_sensor, json = {'ID':1000,'humidity':10.9,'temperature':12.4})
print(r)
data = r.json()
print(data)
