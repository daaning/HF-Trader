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
        print (status)
        time = status[0]
        currency = status [1]
        rep = status[2]
        loopdone = status[3]
        if loopdone:
            BinanceAPI.initiate()

        data = BinanceAPI.get_data(time, currency, rep, loopdone)
        data2 = Stockstats.make_stockstats(data)


        

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
