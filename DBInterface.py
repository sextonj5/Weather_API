import sqlite3
from datetime import datetime


def reformat_list(titles,input_list):
    return [dict(zip(titles, i)) for i in input_list ]
    
def add_sensor(country,city):
    con = sqlite3.connect('Weather.db')
    cur = con.cursor()
    date = int(datetime.timestamp(datetime.now())*1000)
    cur.execute("INSERT INTO sensors (date_added, country, city) VALUES (?,?,?)",(date,country,city))
    con.commit()
    con.close()

def add_sensor_datapoint(sensor_ID, temp, hum):
    con = sqlite3.connect('Weather.db')
    cur = con.cursor()
    date = int(datetime.timestamp(datetime.now())*1000)
    check = cur.execute("SELECT * FROM sensors WHERE ID =:y",{'y':sensor_ID})
    check = check.fetchall()
    if check:
        cur.execute("INSERT INTO sensordata (sensor, temperature, humidity, date) VALUES (?,?,?,?)",(sensor_ID,temp,hum,date))
        con.commit()
        con.close()
    else:
        con.close()
        raise ValueError("Sensor is not registered")
    


def retrieve_data_by_city(city):
    con = sqlite3.connect('Weather.db')
    cur = con.cursor()
    titles = ["Sensor ID", "Timestamp", "Country", "City"]
    cur.execute("SELECT * FROM sensors WHERE city =:y",{'y':city})
    out = reformat_list(titles, cur.fetchall())
    con.close()
    return out
 
        
def retrieve_datapoint_by_time(sensors, start, end, average = False):
    #I have added this if statement in case we want to query data by sensor ID over a date range
    #without returning the humidity or temperature average
    titles = ['data ID', 'Date', 'Sensor ID', 'temperature','humidity']
    con = sqlite3.connect('Weather.db')
    cur = con.cursor()
    if not average:
        cur.execute("SELECT * FROM sensordata WHERE (sensor = ?) AND (date BETWEEN ? AND ?)",(sensors,start,end))
        out = cur.fetchall()
        out = reformat_list(titles, cur.fetchall())
        con.close()
        return out

    else:
        temp = []
        hum = []
        for i in sensors:
            cur.execute("SELECT AVG(humidity) FROM sensordata WHERE (sensor = ?) AND (date BETWEEN ? AND ?)",(i,start,end))
            hum.append(cur.fetchall()[0][0])

        for i in sensors:    
            cur.execute("SELECT AVG(temperature) FROM sensordata WHERE (sensor = ?) AND (date BETWEEN ? AND ?)",(i, start,end))
            temp.append(cur.fetchall()[0][0])
        con.close()
        return {"temperature":dict(zip(sensors,temp)),"humidity":dict(zip(sensors, temp))}
        
