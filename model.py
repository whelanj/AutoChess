
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 20:07:12 2020
"""

from keras.layers import Dense
from keras.layers import Dropout
from keras.models import Sequential
from keras.utils import to_categorical
import numpy as np


class TicTacToeModel:

    def __init__(self, numberOfInputs, numberOfOutputs, epochs, batchSize):
        self.epochs = epochs
        self.batchSize = batchSize
        self.numberOfInputs = numberOfInputs
        self.numberOfOutputs = numberOfOutputs
        self.model = Sequential()
        self.model.add(Dense(81, input_dim=81, activation='relu'))
        self.model.add(Dense(128, activation='relu'))
        self.model.add(Dropout(.50))
        #self.model.add(Dense(128, activation='relu'))
        #self.model.add(Dropout(.50))
        #self.model.add(Dense(128, activation='relu'))
        #self.model.add(Dropout(.50))
        #self.model.add(Dense(128, activation='relu'))
        self.model.add(Dense(3, activation='linear', kernel_initializer='glorot_uniform'))
        self.model.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])

    def train(self, dataset):
        input = []
        output = []
        for data in dataset:
            input.append(data[1])
            output.append(data[0])

        X = np.array(input).reshape((-1, self.numberOfInputs))
        y = to_categorical(output, num_classes=3)
        # Train and test data split
        boundary = int(0.8 * len(X))
        X_train = X[:boundary]
        X_test = X[boundary:]
        y_train = y[:boundary]
        y_test = y[boundary:]
        self.model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=self.epochs, batch_size=self.batchSize)

    def predict(self, data, index):
        return self.model.predict(np.array(data).reshape(-1, self.numberOfInputs))[0][index]
