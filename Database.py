import sqlite3
import Settings

conn = sqlite3.connect('daaaaaata.db')
c = conn.cursor()
databases = []
markets = Settings.tradewith
lenmarket = len(markets)

def create_db():
    for ma in range(4):
        for ti in range(lenmarket):
            databases.append(markets[ti] + "." + str(ma))
    return databases

for ma in range(4):
    for ti in range(lenmarket):
        print (ti + ma * lenmarket)

def new():
    for ma in range(4):
        for ti in range(lenmarket):
            c.execute('''CREATE TABLE %d(
                timestamp REAL,
                open TEXT, 
                high REAL, 
                low REAL, 
                close REAL,
                volume REAL,
                macd REAL,
                signal REAL,
                histogram REAL,
                rsi REAL
                )''' %(databases[ti + ma * lenmarket]))

def insert_into_db(lastLine, time, currency):
    
    c.execute('''INSERT INTO %d VALUES(?,?,?,?,?,?,?,?,?,?)''' %(
        databases[time + currency * lenmarket]), lastLine)
    conn.commit()


# get last entry from database 
def get_last_entry(time, currency):
    c.execute("SELECT * FROM %d ORDER BY id DESC LIMIT 1"%(databases[time + currency * lenmarket]))
    result = c.fetchone()
    print (result)

# get all entries from database 
def get_all_entries(time, currency):
    c.execute("SELECT * FROM %d" %(databases[time + currency * lenmarket])
    result = c.fetchall()
    for res in result:
        print (res)



