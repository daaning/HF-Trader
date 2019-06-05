import binance_api
import twitter_api
import database
import neuralnet
import staticals


if __name__ == "__main__":
    binance_api.fill_database()
    


    while True:
        binance_api.get_data()

        data = database.get_last_data()
        staticals.calculate(data)
        
