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
    for market in range(lenmarket):
        for time in range(lenmarket):
            c.execute('''CREATE TABLE %r
            (id int, timestamp REAL, open REAL, high REAL, low REAL,close REAL,
            volume REAL,macd REAL,signal REAL,histogram REAL,rsi REAL)'''
            %(databases[market + time * lenmarket]))
        

# this function fills up the database
def fill_new_db(time, currency, df):
    
    engine = create_engine("sqlite:///data.db")
    df.to_sql(databases[currency + time * lenmarket],
    engine, if_exists='replace', index=True, index_label="id")


# after the first round this function checks for new data and appends that 
def update_db(time, currency, last_line_df):
    
    last_in_db = get_last_entry(time, currency)
    last_in_pd = last_line_df.values[-1]
    try:
        if int(last_in_pd[0]) != int(last_in_db[1]):
            engine = create_engine("sqlite:///data.db")
            last_line_df.to_sql(databases[currency + time * lenmarket], engine, if_exists='append',
            index=True, index_label="id")
    except:
        print ("Loading db failed, Trying on the next round")


# get last entry from database 
def get_last_entry(time, currency):
    c.execute("SELECT * FROM %r ORDER BY timestamp DESC LIMIT 1" %(
        databases[currency + time * lenmarket]))
    result = c.fetchone()

    return result


# get a set amount of entries from the end of the databanks
def get_xAmount_entry(time, currency, amount):
    c.execute("SELECT * FROM %r ORDER BY timestamp DESC LIMIT " %(databases[currency + time * lenmarket]) + str(amount))
    
    result = c.fetchall()

    return result


# get all entries from database 
def get_all_entries(time, currency):
    c.execute("SELECT * FROM %r" %(
        databases[time + currency * lenmarket]))
    result = c.fetchall()
    
    return result

