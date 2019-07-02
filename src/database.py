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
    CREATE TABLE prices(timestamp INT, open REAL, high REAL, low REAL, close REAL, volume REAL)
''')

c.execute('''
    CREATE TABLE predictions(timestamp INT, x1 REAL, x2 REAL, x3 REAL, x4 REAL, x5 REAL, x6 REAL, x7 REAL)
''')

def insert_data(timestamp, open, high, low, close, volume):
    c.execute('''INSERT INTO prices(timestamp, open, high, low, close, volume)
                  VALUES(?,?,?,?,?,?)''', (timestamp, open, high, low, close, volume))\

                    
def insert_predictions(timestamp, x1, x2, x3, x4, x5, x6, x7):
    c.execute('''INSERT INTO predictions(timestamp, x1, x2, x3, x4, x5, x6, x7)
                  VALUES(?,?,?,?,?,?,?,?)''', (timestamp, x1, x2, x3, x4, x5, x6, x7))


def get_all_data():
    c.execute('''SELECT * FROM prices''')
    user = c.fetchall()
    return user

def get_all_predictions():
    c.execute('''SELECT * FROM predictions''')
    user = c.fetchall()
    return user

def get_conn():
    return conn

def get_data_last(n):
    c.execute("SELECT * FROM prices ORDER BY timestamp DESC LIMIT " + str(n))
    user = c.fetchall()
    return user

def get_predictions_last(n):
    c.execute("SELECT * FROM predictions ORDER BY timestamp DESC LIMIT " + str(n))
    user = c.fetchall()
    return user
