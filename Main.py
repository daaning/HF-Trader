import Settings
import BinanceAPI
import Strategy
import time

timeframes = Settings.timeframes
lenmarkets = len(Settings.tradewith)

# main loop
def main():
    for loop in range(1000):
        status = itter()
        time = status[0]
        currency = status [1]
        rep = status[2]
        loopdone = [3]

        data = BinanceAPI.get_data(time, currency, rep)

        

        print data

time = 0
currency = 0
rep = 0

def itter():
    global time
    global rep
    global currency
    loopdone = False

    time += 1
    if time == len(timeframes):
        currency += 1
        if currency == lenmarkets:
            rep += 1
            loopdone = True

    return time, currency, rep, loopdone





if __name__ == "__main__":
    main()
