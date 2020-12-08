#!/usr/bin/env python
# coding: utf-8

# ### Engine is the file which chooses the model, compiles the data, makes predictions.

# In[123]:


#import importlib
#import import_ipynb
import datetime
import numpy
import pandas
import yfinance as yf
import matplotlib.pyplot as plt

#MY STUFF
import Data
#importlib.reload(Data)
from Data import build_training_set
from Data import build_prediction_set

import Models
#importlib.reload(Models)
from Models import choose_model


# In[1]:


def make_predictions(tickers, date, days_out = 4):
    #This function will return a 1 x len(tickers) array with the predicted closing prices of each ticker on the date given.
    
    predictions = []
    
    for ticker in tickers:
        
        #for Debugging
        print (ticker)
        
        #Choose the model to use. Currently, decision tree is the only available model.
        model = choose_model()
        
        #Compile training data
        #This data includes everything from 2010 - 40 days ago.
        #The Y colum will be the closing prices x days from now, where x = date - today.
        X_train, Y_train = build_training_set(ticker, date, days_out)
        
        #Train the model on the ticker data
        model.fit(X_train, Y_train)
        
        # Compile prediction data.
        # This will include 30 days of closing prices + analytics leading up to today.
        X_predict , Today_Scaled = build_prediction_set(ticker, date, days_out)
        
        #Use the model to predict the price on date
        predict = model.predict(X_predict)
        
        #Add prediction to list along with today's scaled closing price.
        predictions.append([ticker, Today_Scaled, predict[-1]])
        
        
    return predictions
    


# In[ ]:




