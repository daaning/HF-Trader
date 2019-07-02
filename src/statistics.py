import tensorflow as tf
import numpy as np
import main
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import twitter_api
import talib
import random
import sqlite3
import database

first = True
def calculate():
        global first
        dataset = pd.read_sql_query("SELECT * FROM prices ORDER BY timestamp DESC LIMIT 50", database.get_conn())
        dataset = dataset[::-1]
        dataset['H-L'] = dataset['high'] - dataset['low']
        dataset['O-C'] = dataset['close'] - dataset['open']
        dataset['3day MA'] = dataset['close'].shift(1).rolling(window = 3).mean()
        dataset['10day MA'] = dataset['close'].shift(1).rolling(window = 10).mean()
        dataset['30day MA'] = dataset['close'].shift(1).rolling(window = 30).mean()
        dataset['Std_dev']= dataset['close'].rolling(5).std()
        dataset['RSI'] = talib.RSI(dataset['close'].values, timeperiod = 9)
        dataset['MACD'] = talib.MACD(dataset['close'].values, fastperiod=12, slowperiod=26, signalperiod=9)[0]
        dataset['Williams %R'] = talib.WILLR(dataset['high'].values, dataset['low'].values, dataset['close'].values, 7)
        dataset['Price_Rise'] = np.where(dataset['close'].shift(-1) > dataset['close'], 1, 0)
        data = dataset.iloc[:, 4:]
        xlen = data.shape[0]
        ylen = data.shape[1]
        data = data.values
        data_train = data[np.arange(0, xlen), :]
        scaler = MinMaxScaler(feature_range=(-1, 1))
        scaler.fit(data_train)
        data_train = scaler.transform(data_train)

        if not first:
                database.insert_predictions(dataset['timestamp'].iloc[0], data_train[0][1], data_train[0][2],
                 data_train[0][3], data_train[0][4], data_train[0][5], data_train[0][6],
                 data_train[0][7], data_train[0][8], data_train[0][9], data_train[0][10],
                 data_train[0][11], twitter_api.get_sentiment()[0], twitter_api.get_sentiment()[1])
        else:
                for i in range(50):
                        database.insert_predictions(dataset['timestamp'].iloc[i], data_train[i][1],
                         data_train[i][2], data_train[i][3], data_train[i][4], data_train[i][5], 
                         data_train[i][6], data_train[i][7], data_train[i][8], data_train[i][9], 
                         data_train[i][10], data_train[i][11], 0.0, 0.0)

                first = False
        return dataset.iloc[49]