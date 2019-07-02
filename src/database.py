import sqlite3
from sqlalchemy import create_engine
import pandas as pd
import os.path
import json

if os.path.isfile('../data/data.db'): 
    os.remove('../data/data.db')

conn = sqlite3.connect('../data/data.db')
c = conn.cursor()

c.execute('''
    CREATE TABLE prices(timestamp DOUBLE, open REAL, high REAL, low REAL, close REAL, volume REAL)
''')

c.execute('''
    CREATE TABLE predictions(timestamp DOUBLE, x1 REAL, x2 REAL, x3 REAL, x4 REAL,
     x5 REAL, x6 REAL, x7 REAL, x8 REAL, x9 REAL, x10 REAL, x11 REAL, x12 REAL, x13 REAL)
''')

def insert_data(timestamp, open, high, low, close, volume):
    c.execute('''INSERT INTO prices(timestamp, open, high, low, close, volume)
                  VALUES(?,?,?,?,?,?)''', (timestamp, open, high, low, close, volume))

                    
def insert_predictions(timestamp, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13):
    c.execute('''INSERT INTO predictions(timestamp, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13)
                  VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', (timestamp, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13))


def get_all_data():

    c.execute('''SELECT * FROM prices''')
    data = c.fetchall()
    out = [[] for i in range(len(data))]
    for i, entry in enumerate(data):
        out[i].extend(entry)

    return out

def get_all_predictions():

    c.execute('''SELECT * FROM predictions''')
    data = c.fetchall()
    out = [[] for i in range(len(data))]
    for i, entry in enumerate(data):
        out[i].extend(entry)

    return out

def get_conn():
    return conn

def get_data_last(n):

    c.execute("SELECT * FROM prices ORDER BY timestamp desc LIMIT " + str(n))
    data = c.fetchall()
    out = [[] for i in range(len(data))]
    for i, entry in enumerate(data):
        out[i].extend(entry)

    return out

def get_predictions_last(n):

    c.execute("SELECT * FROM predictions ORDER BY timestamp desc LIMIT " + str(n))
    data = c.fetchall()
    out = [[] for i in range(len(data))]
    for i, entry in enumerate(data):
        out[i].extend(entry)

    return out
