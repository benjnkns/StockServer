#!/usr/bin/env python
#https://robin-stocks.readthedocs.io/en/latest/functions.html
# coding: utf-8

# In[1]:


# Python Stuff
import datetime

# My Stuff
import RobinhoodAPI
from RobinhoodAPI import login
from RobinhoodAPI import get_holdings
from RobinhoodAPI import get_funds
from RobinhoodAPI import build_profile
from RobinhoodAPI import purchase_stocks_maximum_amount
from RobinhoodAPI import purchase_stocks_market_order
from RobinhoodAPI import sell_stocks_limit_order
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


my_stocks = get_holdings()

print ("Stocks: ")
print (my_stocks)

for key in list(my_stocks.keys()):
	print("Selling " + str(key) + "...")

	current_market_price = float(get_current_ticker_price(key)[0])
	limit_order_price = current_market_price - 1.00
	print ("Current Market Price = " + str(current_market_price))

	number_stocks_held = my_stocks.get(key).get('quantity')
	print ("Number of Stocks Held: " + str(number_stocks_held))

	
	print ("Selling " + str(number_stocks_held) + " shares of " + str(key) + " at a limit price of " + str(limit_order_price))

	sell_stocks_limit_order(str(key), number_stocks_held, limit_order_price)

# In[22]:


print ("Sell Stocks Completed")

