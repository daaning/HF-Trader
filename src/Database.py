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
    CREATE TABLE prices(timestamp INT, open REAL, sentiment REAL, objectivity REAL)
''')


def insert(timestamp, open, sentiment, objectivity):
    c.execute('''INSERT INTO prices(timestamp, open, sentiment, objectivity)
                  VALUES(?,?,?,?)''', (timestamp, open, sentiment, objectivity))


def get_all():
    c.execute('''SELECT timestamp, open FROM prices''')
    user = c.fetchall()
    return user
