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

def insert_data(timestamp, opens, high, low, close, volume):
    c.execute('''INSERT INTO prices(timestamp, open, high, low, close, volume)
                  VALUES(?,?,?,?,?,?)''', (timestamp, opens, high, low, close, volume))


def get_all_data():
    c.execute('''SELECT * FROM prices''')
    user = c.fetchall()
    return user

def get_conn():
    return conn

def get_data_last(n):
    c.execute("SELECT * FROM prices ORDER BY timestamp DESC LIMIT " + str(n))
    user = c.fetchall()
    return user

