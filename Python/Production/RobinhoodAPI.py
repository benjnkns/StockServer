#!/usr/bin/env python
# coding: utf-8

# In[14]:


import robin_stocks
import pyotp
from robin_stocks import *
# MFA: LQMLQPGPNGQFSOG2
# Bakup: 768783 811148


# In[15]:


def login(username, password):
    totp  = pyotp.TOTP("LQMLQPGPNGQFSOG2").now()
    print("Current OTP:", totp)
    return robin_stocks.robinhood.login(username, password, 86400, mfa_code=totp)


# In[3]:


def get_holdings():
    my_stocks = robin_stocks.robinhood.build_holdings()
    return my_stocks


# In[4]:


def get_funds():
    funds = load_account_profile()
    return funds['cash']


# In[5]:


def get_current_ticker_price(Ticker):
    return robin_stocks.robinhood.get_latest_price(Ticker)


# In[6]:


def build_profile():
    return robin_stocks.robinhood.build_user_profile()


# In[7]:


def load_account_profile():
    return robin_stocks.robinhood.profiles.load_account_profile()


# In[8]:


def purchase_stocks_market_order (Ticker, quantity):
    robin_stocks.robinhood.order_buy_market(Ticker, quantity)
    return 1


# In[9]:


def sell_stocks_market_order (Ticker, quantity):
    robin_stocks.robinhood.order_sell_market(Ticker, quantity)
    return 1


# In[10]:


def sell_stocks_limit_order (Ticker, quantity, limit_price):
    robin_stocks.order_sell_limit(Ticker,quantity,limit_price)
    return 1


# In[11]:


def purchase_stocks_maximum_amount(Ticker):
    current_stock_price = robin_stocks.robinhood.get_latest_price(Ticker)
    current_funds = get_funds()
    stock_purchase_quantity = int(float(current_funds) / float(current_stock_price[0]))
    
    purchase_stocks_market_order (Ticker, stock_purchase_quantity)
    
    return stock_purchase_quantity


# In[19]:


#MFA: JLON5HQTEVQK3VQM
# Bakup: 768783 811148


# In[20]:


#pyotp.TOTP("LQMLQPGPNGQFSOG2").now()


# In[ ]:




