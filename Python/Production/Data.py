#!/usr/bin/env python
# coding: utf-8

# ### This file compiles data.

# In[1]:


import datetime
import numpy
import pandas
import yfinance as yf
from datetime import timedelta
from pandas_datareader import data as pdr
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import scale, StandardScaler

#My Stuff
import Analytics
from Analytics import Simple_Moving_Average 
from Analytics import Simple_Moving_Average_20Day
from Analytics import Relative_Strength_Index
from Analytics import Standard_Deviation
from Analytics import Bandwidth
from Analytics import Rate_Of_Change
from Analytics import Rate_Of_Change_20Day

# Override yFinance with Pandas
yf.pdr_override() # <-- Here is the fix


# In[2]:


def get_ticker_data(ticker, start_date, end_date):
    # Grab data
    data = pdr.get_data_yahoo(str(ticker), start = start_date, end = end_date)
    return data


# In[3]:


def build_training_set(ticker, date, days_out):
    
    data = get_ticker_data(ticker, datetime.datetime(2010, 1, 1), date)
    data = data.values
    
    #days_out = date - datetime.date.today()
    #days_out = days_out.days
    
    closing_prices = scale_data(data[:,3])
    closing_prices_future = closing_prices[days_out:]

    
    # Calculate Analytics
    SMA = Simple_Moving_Average(closing_prices)
    SMA20 = Simple_Moving_Average_20Day(closing_prices)
    RSI = Relative_Strength_Index(closing_prices)
    STD = Standard_Deviation(closing_prices)
    BW = Bandwidth(closing_prices, STD)
    ROC = Rate_Of_Change(closing_prices)
    ROC100 = Rate_Of_Change_20Day(closing_prices)
    
    # Trim Data
    # Trim the first 20 entries because ROC20 is all zeros
    # Trim the last 30 entires.
    SMA    = SMA    [20:-30]
    SMA20  = SMA20  [20:-30]
    RSI    = RSI    [20:-30]
    STD    = STD    [20:-30]
    BW     = BW     [20:-30]
    ROC    = ROC    [20:-30]
    ROC100 = ROC100 [20:-30]
    closing_prices = closing_prices [20:-30]
    closing_prices_future = closing_prices_future[20:-(30 - days_out)]
    
    
    # Reshape Data
    SMA      = numpy.reshape(SMA, (len(SMA), 1))
    SMA20    = numpy.reshape(SMA20, (len(SMA20), 1))
    RSI      = numpy.reshape(RSI, (len(RSI), 1))
    STD      = numpy.reshape(STD, (len(STD), 1))
    BW       = numpy.reshape(BW, (len(BW), 1))
    ROC      = numpy.reshape(ROC, (len(ROC), 1))
    ROC100   = numpy.reshape(ROC100, (len(ROC100), 1))
    closing_prices        = numpy.reshape(closing_prices, (len(closing_prices), 1))
    closing_prices_future = numpy.reshape(closing_prices_future, (len(closing_prices_future), 1))
    

#    print(SMA.shape)
#    print(SMA20.shape)
#    print(RSI.shape)
#    print(STD.shape)    
#    print(BW.shape)
#    print(ROC.shape)    
#    print(ROC100.shape)    
#    print(closing_prices.shape)    
#    print(closing_prices_5_day.shape)    
    
    
    
    X = numpy.concatenate((SMA, SMA20, RSI, STD, BW, ROC, ROC100, closing_prices), axis = 1)
    Y = closing_prices_future
    
    X, x_dont_use, Y, y_dont_use = train_test_split(X, Y, test_size=.001, random_state=47)

#    print(X.shape)
#    print(Y.shape)
    
    return X.astype(int), Y.astype(int)
    


# In[4]:


def build_prediction_set(ticker, date, days_out):
    
    #Get date from 50 days ago until today, because we need to subtrac the first 20 records lol.
    data = get_ticker_data(ticker, date - timedelta(days = 50), date)
    data = data.values
    
    #Calcualte analytics
    closing_prices = scale_data(data[:,3])
    Today_Scaled = closing_prices[-1]
    last_15_days_scaled = closing_prices[-15:]
    
    
    # Calculate Analytics
    SMA = Simple_Moving_Average(closing_prices)
    SMA20 = Simple_Moving_Average_20Day(closing_prices)
    RSI = Relative_Strength_Index(closing_prices)
    STD = Standard_Deviation(closing_prices)
    BW = Bandwidth(closing_prices, STD)
    ROC = Rate_Of_Change(closing_prices)
    ROC100 = Rate_Of_Change_20Day(closing_prices)
    
    # Trim Data
    # Trim the first 20 entries because ROC20 is all zeros
    # Trim the last 30 entires.
    SMA    = SMA    [20:]
    SMA20  = SMA20  [20:]
    RSI    = RSI    [20:]
    STD    = STD    [20:]
    BW     = BW     [20:]
    ROC    = ROC    [20:]
    ROC100 = ROC100 [20:]
    closing_prices = closing_prices [20:]
    
    
    # Reshape Data
    SMA      = numpy.reshape(SMA, (len(SMA), 1))
    SMA20    = numpy.reshape(SMA20, (len(SMA20), 1))
    RSI      = numpy.reshape(RSI, (len(RSI), 1))
    STD      = numpy.reshape(STD, (len(STD), 1))
    BW       = numpy.reshape(BW, (len(BW), 1))
    ROC      = numpy.reshape(ROC, (len(ROC), 1))
    ROC100   = numpy.reshape(ROC100, (len(ROC100), 1))
    closing_prices = numpy.reshape(closing_prices, (len(closing_prices), 1))
    
    

#    print(SMA.shape)
#    print(SMA20.shape)
#    print(RSI.shape)
#    print(STD.shape)    
#    print(BW.shape)
#    print(ROC.shape)    
#    print(ROC100.shape)    
#    print(closing_prices.shape)    
#    print(closing_prices_5_day.shape)    
    
    
    #Build the prediction set.
        
    X = numpy.concatenate((SMA, SMA20, RSI, STD, BW, ROC, ROC100, closing_prices), axis = 1)
    
    return X.astype(int),  Today_Scaled
    


# In[5]:


def scale_data(data):
    return scale(data)
    #return data


# In[6]:


def unscale_data(data):
    return StandardScaler.inverse_scale(data)
    #return data


# In[9]:


# WOOT
#start_date = datetime.datetime(2013, 1, 1)
#end_date   = datetime.datetime(2018, 3, 9)
#get_ticker_data('AAPL', start_date, end_date)


# In[ ]:




