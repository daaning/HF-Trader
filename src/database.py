import sqlite3
from sqlalchemy import create_engine
import pandas as pd
import os.path
import json

if os.path.isfile('data/data.db'): 
    os.remove('data/data.db')

conn = sqlite3.connect('data/data.db')
c = conn.cursor()

c.execute('''
    CREATE TABLE prices(timestamp INT, opens REAL, high REAL, low REAL, close REAL, volume REAL)
''')

c.execute('''
    CREATE TABLE predictions(timestamp INT, rsi REAL, macd REAL, sar REAL, adosc REAL, aroon REAL, ult REAL, sent REAL, obj REAL)
''')

def insert_data(timestamp, opens, high, low, close, volume):
    c.execute('''INSERT INTO prices(timestamp, opens, high, low, close, volume)
                  VALUES(?,?,?,?,?,?)''', (timestamp, opens, high, low, close, volume))

def insert_predictions(timestamp, rsi, macd, sar, adosc, aroon, ult, sent, obj):
    c.execute('''INSERT INTO predictions(timestamp, rsi, macd, sar, adosc, aroon, ult, sent, obj)
                  VALUES(?,?,?,?,?,?,?,?,?)''', (timestamp, rsi, macd, sar, adosc, aroon, ult, sent, obj))


def get_all_data():
    c.execute('''SELECT * FROM prices''')
    user = c.fetchall()
    return user

def get_last_data(n):
    c.execute("SELECT * FROM prices ORDER BY timestamp DESC LIMIT " + str(n))
    user = c.fetchall()
    return user

def get_predictions():
    c.execute('''SELECT * from predictions''')
    user = c.fetchall()
    return user

