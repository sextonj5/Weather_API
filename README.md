# Weather_API
## Dependencies
* Flask
* Pytest
* Sqlite3

## Structure
### Weather.db
An SQLite DB containing two tables:
* sensor - contains a list of sensors and their locations (city and country) There is an automatically generated Unique Primary key id for each sensor. Each sensor also has a time stamp in unix time corresponding to the time when it was first added to the DB.

* sensordata - contains a list of sensor readings (temperature and humidity) There is an automatically generated Unique Primary key id for each sensor reading. Each reading also has a time stamp in unix time.

### Http.py
This file containes each of the 4 Rest endpoints (GET /senor, POST /sensor, GET /sensordata, POST /sensordata)
