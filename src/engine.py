
import binanceAPI
import server
import time

if __name__ == "__main__":
    binanceAPI.fill_database()
    server.start()
