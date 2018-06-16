import Settings
import BinanceAPI
import Strategy
import time
import Stockstats
import Database
import Strategy
from multiprocessing import Pool

timeframes = Settings.timeframes
markets = Settings.tradewith
lenmarkets = len(markets)

def main():
    print(50*"#")
    print("Starting main process")
    Database.create_db()

    while True:
        status = itter()
        time = status[0]
        currency = status [1]
        rep = status[2]
        loopdone = status[3]
        timeloopdone = status[4]
        

        if loopdone:
            BinanceAPI.initiate()
        df = BinanceAPI.get_data(time, currency, rep, loopdone)

        if rep != 0:
            Database.update_db(time, currency, df.tail(-1))
            print (time, markets[currency])
            Strategy.run(df, time, currency, rep, loopdone, timeloopdone)

        else:
            Database.fill_new_db(time, currency, df)
            print("Filling up db for: " +  markets[currency] + " " + timeframes[time])
        
        
        

time = -1
currency = 0
rep = 0
"""
Itterration function that addapts to the number of currencies and timeframes

"""
def itter():
    global time
    global rep
    global currency
    loopdone = False
    timeloop = False
    time += 1
    if time == 4:
        currency += 1
        time = 0
        timeloop = True
        if currency == lenmarkets:
            currency = 0
            rep += 1
            loopdone = True

    return time, currency, rep, loopdone, timeloop




if __name__ == "__main__":
    main()
