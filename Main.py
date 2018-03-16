import Settings
import BinanceAPI
import Strategy
lenmarket = len(Settings.tradewith)
timeframe = Settings.timeframe
import time
"""
def main():
    database.make()
    API.getHistoricaldata()

    for i in range(runlength):
        state = itter()
        API.get_data(state)
"""

def main():
    for ma in range(1000):
        status = itter()
        i = status[0]
        rep = status[1]
        loopdone = [2]

        data = BinanceAPI.get_data(i, rep)
        judgement = Strategy.run(i, rep, loopdone, data)
        print (judgement)

        if loopdone:
            time.sleep(Settings.timeframe)




i = -1
rep = 0
def itter():
    global rep
    global i
    loopdone = False
    i += 1
    if i == lenmarket:
        i = 0
        rep += 1
        loopdone = True

    return i, rep, loopdone





if __name__ == "__main__":
    main()
