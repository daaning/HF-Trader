import tensorflow as tf
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import talib
import random
import sqlite3
import database



# Importing dataset
def load_data():
        dataset = pd.read_sql_query("SELECT * FROM prices ORDER BY timestamp DESC LIMIT 1000", database.get_conn())

        timestamps = dataset['timestamp'].tolist()
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

        return dataset, timestamps
        


def run(dataset, timestamps):

        data = dataset.iloc[:, 4:]
        # Dimensions of data
        n = data.shape[0]
        p = data.shape[1]
        # Make data a np.array
        data = data.values

        # Splitting the dataset- Training and test data
        train_start = 0
        train_end = int(np.floor(0.8*n))
        test_start = train_end + 1
        test_end = n
        data_train = data[np.arange(train_start, train_end), :]
        data_test = data[np.arange(test_start, test_end), :]

        print(data_test[0])
        # Scale data
        scaler = MinMaxScaler(feature_range=(-1, 1))
        scaler.fit(data_train)
        data_train = scaler.transform(data_train)
        data_test = scaler.transform(data_test)

        # Build X and y
        X_train = data_train[:, 0:-1]
        y_train = data_train[:, -1]
        X_test = data_test[:, 0:-1]
        y_test = data_test[:, -1]

        # Building the Artificial Neural Network:
        # Number of features in training data
        n_features = X_train.shape[1]

        # Neurons
        n_neurons_1 = 512
        n_neurons_2 = 256
        n_neurons_3 = 128

        # Session
        net = tf.InteractiveSession()

        # Placeholder
        X = tf.placeholder(dtype=tf.float32, shape=[None, n_features])
        Y = tf.placeholder(dtype=tf.float32, shape=[None])

        # Initializers
        sigma = 1
        weight_initializer = tf.variance_scaling_initializer(mode="fan_avg", distribution="uniform", scale=sigma)
        bias_initializer = tf.zeros_initializer()

        # Hidden weights:
        #Layer 1: Variables for hidden weights and biases
        W_hidden_1 = tf.Variable(weight_initializer([n_features, n_neurons_1]))
        bias_hidden_1 = tf.Variable(bias_initializer([n_neurons_1]))
        #Layer 2: Variables for hidden weights and biases
        W_hidden_2 = tf.Variable(weight_initializer([n_neurons_1, n_neurons_2]))
        bias_hidden_2 = tf.Variable(bias_initializer([n_neurons_2]))
        #Layer 3: Variables for hidden weights and biases
        W_hidden_3 = tf.Variable(weight_initializer([n_neurons_2, n_neurons_3]))
        bias_hidden_3 = tf.Variable(bias_initializer([n_neurons_3]))

        # Output weights:
        #Output layer: Variables for output weights and biases
        W_out = tf.Variable(weight_initializer([n_neurons_3, 1]))
        bias_out = tf.Variable(bias_initializer([1]))

        # Hidden layer
        hidden_1 = tf.nn.relu(tf.add(tf.matmul(X, W_hidden_1), bias_hidden_1))
        hidden_2 = tf.nn.relu(tf.add(tf.matmul(hidden_1, W_hidden_2), bias_hidden_2))
        hidden_3 = tf.nn.relu(tf.add(tf.matmul(hidden_2, W_hidden_3), bias_hidden_3))

        # Output layer (transpose!)
        out = tf.transpose(tf.add(tf.matmul(hidden_3, W_out), bias_out))

        # Cost function
        mse = tf.reduce_mean(tf.squared_difference(out, Y))

        # Optimizer
        opt = tf.train.AdamOptimizer().minimize(mse)

        # Run initializer
        net.run(tf.global_variables_initializer())

        # Fitting the neural network
        batch_size = 1000
        epochs = 110
        # Run
        for e in range(epochs):
                # Shuffle training data
                shuffle_data = np.random.permutation(np.arange(len(y_train)))
                X_train = X_train[shuffle_data]
                y_train = y_train[shuffle_data]
                # Minibatch training
                for i in range(0, len(y_train) // batch_size):
                        start = i * batch_size
                        batch_x = X_train[start:start + batch_size]
                        batch_y = y_train[start:start + batch_size]
                        # Run optimizer with batch
                        net.run(opt, feed_dict={X: batch_x, Y: batch_y})
                
                

        #Predicting the movement of the stock
        pred = net.run(out, feed_dict={X: X_test})
        y_pred = pred[0]



        #Plotting the graph of returns
        plt.figure(figsize=(10,5))
        plt.plot([i for i in range(len(data_test[:,0]))], data_test[:,0], color='r')
        plt.plot([i for i in range(len(y_pred))], y_pred, color='g')
        plt.legend()
        plt.show()