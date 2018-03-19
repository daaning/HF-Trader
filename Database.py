import sqlite3
from sqlalchemy import create_engine
import Settings

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

def insert_into_db(df, time, currency):
    engine = create_engine("sqlite:///data.db")
    df.to_sql(databases[time + currency * lenmarket], engine, if_exists='append', index=False)
    
    

# get last entry from database 
def get_last_entry(time, currency):
    c.execute("SELECT * FROM %r ORDER BY timestamp DESC LIMIT 1" %(
        databases[time + currency * lenmarket]))
    result = c.fetchone()
    print (result)

# get all entries from database 
def get_all_entries(time, currency):
    c.execute("SELECT * FROM %r" %(
        databases[time + currency * lenmarket]))
    result = c.fetchall()
    for res in result:
        print (res)

