import binance_api
import twitter_api
import database
import stats
import time
import statistics
import graph


timeframe = 300
n_data    = 40

if __name__ == "__main__":
    binance_api.fill_database()
    
    while True:
        binance_api.get_data()
        stamp = statistics.calculate()


        time.sleep(60)

