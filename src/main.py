import binance_api
import twitter_api
import database
import neuralnet
import stats
import time
import graph


timeframe = 300
data_amount = 40


if __name__ == "__main__":
    binance_api.fill_database()
    
    while True:
        binance_api.get_data()
        data = database.get_last_data(data_amount)
        statisics = stats.calculate(data)
        print(statisics)
        time.sleep(300)

