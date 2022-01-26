# Weather_API
## Dependencies
* Flask
* Pytest
* Sqlite3

## How to run
(The below setup is for running on MS Windows. Linux and MacOS setups differ slightly but go beyond the scope of the project)
* In the command line navigate to the root directory of this project
* run the following commands:
    set FLASK_APP=HTTP.py
    set FLASK_ENV=development
    flask run
 * To run integration testing open a new command line and navigate to the root directory of this project
 * Run the following command:
    pytest ./Tests.py
 * More advanced testcases can be ran using the following command
    python Client_Test.py

## Structure
### Weather.db
An SQLite DB containing two tables:
* sensor - contains a list of sensors and their locations (city and country) There is an automatically generated Unique Primary key id for each sensor. Each sensor also has a time stamp in unix time corresponding to the time when it was first added to the DB.

* sensordata - contains a list of sensor readings (temperature and humidity) There is an automatically generated Unique Primary key id for each sensor reading. Each reading also has a time stamp in unix time.

### Http.py
This file containes each of the 4 Http Rest endpoints 
* GET /senor
* POST /sensor
* GET /sensordata
* POST /sensordata

### Tests.py
This file contains 8 test cases implemented in pytest

### CreateDB.py
The commands used to intialise the DB and both tables (sensors and sensordata)

### ClientTest.py
This file contains more test cases which are not implemented in pytest, due to the time contraints of the project it was easier to check the output of the code vy eye rather than with pytest. This file was written at the beginning of the project to set a goal for the functionality I wanted the final code to have.

### DBInterface
This File contains data functions which interface with the DB. When a get or post request is handled by the flask app the request data is inputted into the corresponding function in this file. 
