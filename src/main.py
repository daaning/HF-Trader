import binance_api
import twitter_api
import database
import stats
import time
import neuralnet


timeframe = 300
n_data = 40


if __name__ == "__main__":
    binance_api.fill_database()
    
    while True:
        binance_api.get_data()
        data = database.get_data_last(n_data)
        ndataset, timestamps = neuralnet.load_data()
        neuralnet.run(ndataset, timestamps)


        time.sleep(20)

