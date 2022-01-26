import sqlite3
con = sqlite3.connect('Weather.db')
cur = con.cursor()

try:
    cur.execute('''CREATE TABLE sensors(id INTEGER PRIMARY KEY, date_added INTEGER, country text, city text)''')
    cur.execute('''CREATE TABLE sensordata(id INTEGER PRIMARY KEY, date INTEGER, sensor INTEGER, temperature REAL, humidity REAL)''')
except:
    print('failed to create DB tables')
con.close()
