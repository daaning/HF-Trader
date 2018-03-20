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
           

def fill_new_db(df, time, currency):
    engine = create_engine("sqlite:///data.db")
    df.to_sql(databases[currency + time * lenmarket],
     engine, if_exists='replace', index=True, index_label="id")


def update_db(last_line_df, time, currency):
    last_in_db = get_last_entry(time, currency)
    last_in_pd = last_line_df.values[-1]
    
    if int(last_in_pd[0]) == int(last_in_db[1]):
        print ("not adding same data")
    else:
        print("not equal")
        engine = create_engine("sqlite:///data.db")
        last_line_df.to_sql(databases[currency + time * lenmarket], engine, if_exists='append',
        index=True, index_label="id")

        """

        c.execute('''INSERT INTO %r VALUES(?,?,?,?,?,?,?,?,?,?)''' %(
            databases[time + currency * lenmarket]), values)
        conn.commit()
        """

# get last entry from database 
def get_last_entry(time, currency):
    c.execute("SELECT * FROM %r ORDER BY timestamp DESC LIMIT 1" %(
        databases[currency + time * lenmarket]))
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

print(len(get_all_entries(0,3)))