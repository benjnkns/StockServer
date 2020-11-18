#!/usr/bin/env python
# coding: utf-8

# In[1]:


import robin_stocks
from robin_stocks import *


# In[2]:


def login(username, password):
    return robin_stocks.login(username, password)


# In[3]:


def get_holdings():
    my_stocks = robin_stocks.build_holdings()
    return my_stocks


# In[4]:


def get_funds():
    funds = build_profile()
    return funds['cash']


# In[5]:


def get_current_ticker_price(Ticker):
    return robin_stocks.get_latest_price(Ticker)


# In[6]:


def build_profile():
    return robin_stocks.build_user_profile()


# In[7]:


def purchase_stocks_market_order (Ticker, quantity):
    robin_stocks.order_buy_market(Ticker, quantity)


# In[8]:


def sell_stocks_market_order (Ticker, quantity):
    robin_stocks.order_sell_market(Ticker, quantity)


# In[9]:


def sell_stocks_limit_order (Ticker, quantity, limit_price):
    #robin_stocks.order_sell_limit(Ticker,quantity,limit_price)
    return 1


# In[10]:


def purchase_stocks_maximum_amount(Ticker):
    current_stock_price = robin_stocks.get_latest_price(Ticker)
    current_funds = get_funds()
    stock_purchase_quantity = int(float(current_funds) / float(current_stock_price[0]))
    print ("Current funds = " + str(current_funds))
    print ("Current stock price = " + str(current_stock_price))
    #purchase_stocks_market_order (Ticker, stock_purchase_quantity)
    
    return stock_purchase_quantity


# In[11]:


#http://www.robin-stocks.com/en/latest/quickstart.html

