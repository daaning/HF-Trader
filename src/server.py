import sqlite3 as sql
from flask import Flask, render_template
from sqlalchemy import create_engine
import pandas as pd
import os.path
import json

app = Flask(__name__)
if os.path.isfile('../data/data.db'):
    os.remove('../data/data.db')

conn = sql.connect('../data/data.db')
c = conn.cursor()

c.execute('''
    CREATE TABLE prices(timestamp TEXT, open TEXT)
''')


def get():
    c.execute('''SELECT * FROM prices''')
    data = c.fetchall()
    print(data)
    return str(data)


def insert(timestamp, open):
    c.execute('''INSERT INTO prices(timestamp, open)
                  VALUES(?,?)''', (timestamp, open))


@app.route('/init')
def get_all():
    with sql.connect("../data/data.db") as conn:
        d = conn.cursor()
        d.execute('''SELECT * FROM prices''')
        data = d.fetchall()
        print(data)
        return str(data)


def start():
    app.run(port=5000, debug=True)
