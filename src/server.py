import sqlite3 as sql
from flask import Flask, render_template
import sqlite3
from sqlalchemy import create_engine
import pandas as pd
import os.path
import json

app = Flask(__name__)
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


@app.route('/data/<int:n>')
def get(n):
    with sql.connect("../data/data.db") as con:
        c = con.cursor()
        c.execute('''SELECT * FROM prices ORDER BY timestamp DESC LIMIT 1;''')
        return str(c.fetchone())


@app.route('/init')
def get_all():
    with sql.connect("../data/data.db") as con:
        c = con.cursor()
        c.execute('''SELECT * FROM prices ORDER BY timestamp;''')
        return str(c.fetchall())


# run the application
def start():
    app.run(port=5000, debug=True)
