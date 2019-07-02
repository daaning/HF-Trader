import binance_api
import twitter_api
import database
import time
import statistics
import lstm



timeframe = 300
n_data    = 40

if __name__ == "__main__":
    binance_api.fill_database()
    lstm.run()
    
    while True:
        binance_api.get_data()
        stamp = statistics.calculate()
        lstm.update_model()
        print("Timestamp " + str(stamp) + " added ...")
        time.sleep(60)

