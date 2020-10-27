#!/usr/bin/env python
# coding: utf-8

# In[2]:


import robin_stocks
from robin_stocks import *


# In[30]:


def login(username, password):
    #robin_stocks.login("benjnkns@gmail.com","Guitarist474747123")
    return robin_stocks.login(username, password)


# In[32]:


def get_holdings():
    my_stocks = robin_stocks.build_holdings()
    return my_stocks


# In[39]:


def get_funds():
    funds = build_profile()
    return funds['cash']


# In[36]:


def get_current_ticker_price(Ticker):
    return robin_stocks.get_latest_price(Ticker)




def build_profile():
    return robin_stocks.build_user_profile()


# In[43]:


def purchase_stocks_market_order (Ticker, quantity):
    robin_stocks.order_buy_market(Ticker, quantity)


# In[44]:


def sell_stocks_market_order (Ticker, quantity):
    robin_stocks.order_sell_market(Ticker, quantity)


# In[45]:


def sell_stocks_limit_order (Ticker, quantity, limit_price):
    robin_stocks.order_sell_limit(Ticker,quantity,limit_price)


# In[66]:


def purchase_stocks_maximum_amount(Ticker):
    current_stock_price = robin_stocks.get_latest_price(Ticker)
    current_funds = get_funds()
    stock_purchase_quantity = int(float(current_funds) / float(current_stock_price[0]))
    
    #purchase_stocks_market_order (Ticker, stock_purchase_quantity)
    
    return stock_purchase_quantity


# In[62]:


#http://www.robin-stocks.com/en/latest/quickstart.html

