#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Python Stuff
#import import_ipynb
#import importlib
import datetime
from sklearn.tree import DecisionTreeRegressor 

# My Stuff
import Model
from Model import train_model
from Model import build_test_data

import Analytics

import RobinhoodAPI
#importlib.reload(RobinhoodAPI)
from RobinhoodAPI import login
from RobinhoodAPI import get_holdings
from RobinhoodAPI import get_funds
from RobinhoodAPI import build_profile
from RobinhoodAPI import purchase_stocks_maximum_amount
from RobinhoodAPI import get_current_ticker_price


# In[2]:


date = datetime.date.today()


# In[3]:


StockTickers = ['AAPL', 'CCL', 'EBAY', 'GLW', 'KO']


# In[4]:


# Robinhood
print ("Loggin into Robinhood...")
login("benjnkns@gmail.com", "Guitarist474747123")


# In[5]:


RobinhoodProfile = build_profile()
print ("Robinhood Profile: ")
print (RobinhoodProfile)
print ("Starting Cash: " + str(get_funds()))
holdings = get_holdings()
print ("Holdings: ")
print (holdings)


# In[6]:


# create a regressor object 
model1 = DecisionTreeRegressor(random_state = 0) 
model2 = DecisionTreeRegressor(random_state = 0) 
model3 = DecisionTreeRegressor(random_state = 0) 
model4 = DecisionTreeRegressor(random_state = 0) 
model5 = DecisionTreeRegressor(random_state = 0) 
    
# train our master model
#for ticker in StockTickers:
model1 = train_model (model1, StockTickers[0])
model2 = train_model (model2, StockTickers[1])
model3 = train_model (model3, StockTickers[2])
model4 = train_model (model4, StockTickers[3])
model5 = train_model (model5, StockTickers[4])


# In[7]:


stock_data = build_test_data(StockTickers)


# In[8]:


print ( "Current Closing Price " + StockTickers[0] + ": " + str(get_current_ticker_price(StockTickers[0])))
print ( "Current Closing Price " + StockTickers[1] + ": " + str(get_current_ticker_price(StockTickers[1])))
print ( "Current Closing Price " + StockTickers[2] + ": " + str(get_current_ticker_price(StockTickers[2])))
print ( "Current Closing Price " + StockTickers[3] + ": " + str(get_current_ticker_price(StockTickers[3])))
print ( "Current Closing Price " + StockTickers[4] + ": " + str(get_current_ticker_price(StockTickers[4])))


# In[9]:


total_gains_1 = model1.predict(stock_data[0:len(stock_data), 0:8])[-1] - stock_data[len(stock_data)-1, 7]
total_gains_2 = model2.predict(stock_data[0:len(stock_data), 8:16])[-1] - stock_data[len(stock_data)-1, 15]
total_gains_3 = model3.predict(stock_data[0:len(stock_data), 16:24])[-1] - stock_data[len(stock_data)-1, 23]
total_gains_4 = model4.predict(stock_data[0:len(stock_data), 24:32])[-1] - stock_data[len(stock_data)-1, 31]
total_gains_5 = model5.predict(stock_data[0:len(stock_data), 32:40])[-1] - stock_data[len(stock_data)-1, 39]
    
    
maximum_gains = max(total_gains_1, total_gains_2, total_gains_3, total_gains_4, total_gains_5)
    
print (StockTickers[0] + " is predicted to gain $" + str(total_gains_1))
print (StockTickers[1] + " is predicted to gain $" + str(total_gains_2))
print (StockTickers[2] + " is predicted to gain $" + str(total_gains_3))
print (StockTickers[3] + " is predicted to gain $" + str(total_gains_4))
print (StockTickers[4] + " is predicted to gain $" + str(total_gains_5))


# In[10]:


if (maximum_gains < 0):
    print ("Sorry, better luck next week")
    exit()
elif (maximum_gains == total_gains_1):
    ticker_to_buy = StockTickers[0]
elif (maximum_gains == total_gains_2):
    ticker_to_buy = StockTickers[1]
elif (maximum_gains == total_gains_3):
    ticker_to_buy = StockTickers[2]
elif (maximum_gains == total_gains_4):
    ticker_to_buy = StockTickers[3]
elif (maximum_gains == total_gains_5):
    ticker_to_buy = StockTickers[4]
else:
    print ("What.....")


# In[11]:


stocks_purchased = purchase_stocks_maximum_amount(ticker_to_buy)


# In[12]:


print ("Purchased " + str(stocks_purchased) + " stock(s) of " + ticker_to_buy )


# In[13]:


print ("Buy Stocks Completed")

