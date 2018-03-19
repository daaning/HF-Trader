import Settings
import BinanceAPI
import Strategy
import time
import Stockstats
from monary import Monary
from pymongo import MongoClient

timeframes = Settings.timeframes
lenmarkets = len(Settings.tradewith)

def write_df_to_mongoDB(  my_df,\
                          database_name = 'trader' ,\
                          collection_name = 'data',\
                          server = 'localhost',\
                          mongodb_port = 27017):
    client = MongoClient()
    db = client[database_name]
    collection = db[collection_name]
    collection.insert_many(my_df.to_dict('records'))
def main():
    print(50*"#")
    print("Starting main process")

    while True:
        status = itter()
        time = status[0]
        currency = status [1]
        rep = status[2]
        loopdone = [3]

        data = BinanceAPI.get_data(time, currency, rep)
        print(20*"#"+"Binance data"+20*"#")
        print(data)
        write_df_to_mongoDB(data)

        data2 = Stockstats.make_stockstats(data)
        print(20*"#"+"Stockstats data"+20*"#")

        print(data2)
        

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
