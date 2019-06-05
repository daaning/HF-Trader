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
    CREATE TABLE prices(timestamp INT, opens REAL, high REAL, low REAL, close REAL, volume REAL, sentiment REAL, objectivity REAL)
''')

c.execute('''
    CREATE TABLE predictions(timestamp INT, macd REAL, rsi REAL, adx REAL, stochastic REAL, sentiment REAL, machine REAL, tsne REAL)
''')

def insert_data(timestamp, opens, high, low, close, volume, sentiment, objectivity):
    c.execute('''INSERT INTO prices(timestamp, opens, high, low, close, volume)
                  VALUES(?,?,?,?,?,?)''', (timestamp, opens, high, low, close, volume))

def insert_predictions(timestamp, macd, rsi, adx, stochastic, sentiment, machine, tsne):
    c.execute('''INSERT INTO prices(timestamp, macd, rsi, adx, stochastic, sentiment, machine, tsne)
                  VALUES(?,?,?,?,?,?,?)''', (timestamp, macd, rsi, adx, stochastic, sentiment, machine, tsne))


def get_all_data():
    c.execute('''SELECT * FROM prices''')
    user = c.fetchall()
    return user

def get_last_data():
    c.execute('''SELECT * FROM prices ORDER BY timestamp DESC LIMIT 20''')
    user = c.fetchall()
    return user

def get_predictions():
    c.execute('''SELECT * from predictions''')
    user = c.fetchall()
    return user

