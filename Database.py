import sqlite3
from sqlalchemy import create_engine
import Settings
import pandas as pd

conn = sqlite3.connect('data.db')

c = conn.cursor()
databases = []

markets = Settings.tradewith
lenmarket = len(markets)
for ma in range(4):
    for ti in range(lenmarket):
        databases.append(markets[ti] + "." + str(ma))

def create_db():
    for ma in range(4):
        for ti in range(lenmarket):
    

            c.execute('''CREATE TABLE %r
            (timestamp REAL, open REAL, high REAL, low REAL,close REAL,
            volume REAL,macd REAL,signal REAL,histogram REAL,rsi REAL)'''
            %(databases[ti + ma * lenmarket]))

def fill_new_db(df, time, currency):
    engine = create_engine("sqlite:///data.db")
    df.to_sql(databases[time + currency * lenmarket], engine, if_exists='append', index=False)

def update_db(last_line, time, currency):
    last_in_db = get_last_entry(time, currency)
    last_in_pd = last_line.values[-1]
    print (last_in_pd)

    if last_in_db[0] != last_in_pd[0]:
        c.execute('''INSERT INTO %r VALUES(?,?,?,?,?,?,?,?,?,?)''' %(
            databases[time + currency * lenmarket]))
    conn.commit()

# get last entry from database 
def get_last_entry(time, currency):
    c.execute("SELECT * FROM %r ORDER BY timestamp DESC LIMIT 1" %(
        databases[time + currency * lenmarket]))
    result = c.fetchone()

    return result

# get all entries from database 
def get_all_entries(time, currency):
    c.execute("SELECT * FROM %r" %(
        databases[time + currency * lenmarket]))
    result = c.fetchall()
    for res in result:
        print (res)
        
    return result


