import binance_api
import twitter
import database
import neuralnet



if __name__ == "__main__":
    binance_api.fill_database()
    


    while True:
        binance_api.get_data()