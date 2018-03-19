import Settings
import BinanceAPI
import Strategy
import time
import Stockstats
import Database


timeframes = Settings.timeframes
lenmarkets = len(Settings.tradewith)



def main():
    print(50*"#")
    print("Starting main process")
    Database.create_db()
    while True:
        
        status = itter()
        print (status)
        time = status[0]
        currency = status [1]
        rep = status[2]
        loopdone = status[3]
        if loopdone:
            BinanceAPI.initiate()

        data = BinanceAPI.get_data(time, currency, rep, loopdone)

        if rep != 0:
            last_line = Stockstats.make_stockstats(data)
            Database.update_db(last_line, time, currency)
            
        else:
            data2 = Stockstats.make_stockstats(data)
            Database.fill_new_db(data2, time, currency)
            
        
        

        

time = -1
currency = 0
rep = 0

def itter():
    global time
    global rep
    global currency
    loopdone = False

    time += 1
    if time == 4:
        currency += 1
        time = 0
        if currency == lenmarkets:
            currency = 0
            rep += 1
            loopdone = True

    return time, currency, rep, loopdone




if __name__ == "__main__":
    main()
