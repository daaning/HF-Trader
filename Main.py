import Settings
import BinanceAPI
lenmarket = len(Settings.tradewith)
timeframe = Settings.timeframe
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
        print (BinanceAPI.get_data(status[0], status[1]))
        

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
