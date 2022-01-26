from flask import Flask, request, jsonify
import sys
import json
from DBInterface import add_sensor, add_sensor_datapoint, retrieve_data_by_city, retrieve_datapoint_by_time
app = Flask(__name__)

@app.post("/sensor")
def post_sensor():
    if request.is_json:
        try:
            sensor = request.get_json()
            sensor_city = sensor['city']
            sensor_country = sensor['country']
            add_sensor(sensor_country, sensor_city)
            return sensor, 201
        except:
            print(sys.exc_info())
            return {"error": "Could not register sensor into the database"}, 400
    return {"error": "Request must be JSON"}, 415

@app.post("/sensordata")
def post_sensordata():
    if request.is_json:
        try:
            sensor = request.get_json()
            sensor_ID = sensor['ID']
            sensor_hum = sensor['humidity']
            sensor_temp = sensor['temperature']
            add_sensor_datapoint(sensor_ID, sensor_temp, sensor_hum)
            return sensor, 201
        except:
            print(sys.exc_info())
            return {"error": "Could not input sensor data into the database, please ensure the sensor ID is registered"}, 400
    return {"error": "Request must be JSON"}, 415

@app.get("/sensor")
def get_sensor():
    try:
        sensor_city = request.args.to_dict()['city']
        out = jsonify(retrieve_data_by_city(sensor_city))
        return out, 200
    except:
        print(sys.exc_info())
        return {"failed to retrieve item from":" sensor DB"},400

@app.get("/sensordata")
def get_sensordata():
    try:
        sensor_ID = json.loads(request.args.to_dict()['ID'])
        sensor_start = request.args.to_dict()['start']
        sensor_end = request.args.to_dict()['end']
        data = jsonify(retrieve_datapoint_by_time(sensor_ID,sensor_start,sensor_end,True))
        return data, 200
    except:
        print(sys.exc_info())
        return {"failed to retrieve item from":"sensor data DB"}
