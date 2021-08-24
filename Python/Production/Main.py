#!/usr/bin/env python
# coding: utf-8

# In[19]:


import datetime
from datetime import timedelta
import time

# MY STUFF
import RobinhoodAPI
from RobinhoodAPI import login
from RobinhoodAPI import get_holdings
from RobinhoodAPI import get_funds
from RobinhoodAPI import build_profile
from RobinhoodAPI import purchase_stocks_maximum_amount
from RobinhoodAPI import sell_stocks_limit_order
from RobinhoodAPI import get_current_ticker_price

import Engine #Is this how Tesla does it?
from Engine import make_predictions


# In[21]:


#Tickers to evaluate
tickers = ['ATVI','BABA','GOOGL','AMZN','AMC','AMD','AAL','AAPL','T','ACB','BAC','BYND','BA','BP','CGC','CCL','CPRX','KO','CRON','PLAY','DAL','GUSH','DIS','DKNG','ET','XOM','FB','F','FCEL','GE','GILD','GM','GPRO','HAL','HEXO','INO','INTC','IVR','JBLU','JNJ','JPM','KODK','KOS','LYFT','MRO','MFA','MGM','MSFT','MRNA','NFLX','NRZ','NKE','NKLA','NTDOY','NIO','NOK','NCLH','NVDA','OGI','PYPL','PTON','PENN','PFE','PLUG','SPHD','UCO','PSEC','RKT','RCL','SIRI','WORK','SNAP','SRNE','LUV','SPY','SAVE','SQ','SBUX','TCEHY','TSLA','TXMD','TLRY','TWTR','UBER','UAL','USO','VOO','VTI','SPCE','V','WMT','WFC','WKHS','ZM','ZNGA']


# In[25]:


def buy():
    
    #log into robinhood
    print (datetime.date.today())
    print ("Loggin into Robinhood...")
    login("benjnkns@gmail.com", "4tpHFM0c646kponZN")
    time.sleep(2)
    #analyze the market
    print ("Analyzing the Market...")
    print ("Making predictions...")
    try:
        predictions = make_predictions(tickers, datetime.date.today(), 10)
    except:
        print("Error while making predictions..")
    #decide which stock to buy
    total_gains = []
    for i in range(0, len(predictions)):
        total_gains.append(predictions[i][2] - predictions[i][1])
        print (tickers[i] + "is expected to gain " + str(total_gains[i]))
    max_gain = max(total_gains)
    stock_to_purchase = tickers[total_gains.index(max_gain)]
    
    #purchase the stock
    if (max_gain > 0):
        stocks_purchased = purchase_stocks_maximum_amount(stock_to_purchase)
    else:
        stocks_purchased = 0
        
    #print summary
    print ("Purchased " + str(stocks_purchased) + " stocks of " + stock_to_purchase)


# In[26]:


def sell () :

    #log into robinhood
    print (datetime.date.today())
    print ("Loggin into Robinhood...")
    login("benjnkns@gmail.com", "4tpHFM0c646kponZN")
    
    #Display Profile Status
    RobinhoodProfile = build_profile()
    print ("\nRobinhood Profile: ")
    print (RobinhoodProfile)
    
    #Get stocks
    holdings = get_holdings()
    print ("\nHoldings: ")
    for holding in holdings:
        print (holding + " " + str(holdings[holding]) + '\n')
    
    
    #sell all positions 
    #NOTE: If you want to, you could exclude certain positions in this statement to avoid selling them.
    #OR just like, sell all AAPL, MCK, ETC, ... you know, like the 5 stocks I'm analyzing.
    
    for ticker in holdings:
        if (ticker in tickers): 
            #Calculate how many shares to sell and at what price.
            current_market_price = float(get_current_ticker_price(ticker)[0])
            limit_order_price = current_market_price - 1.00
            number_stocks_held = holdings.get(ticker).get('quantity')
            
            #sell stocks
            sell_stocks_limit_order(ticker, number_stocks_held, limit_order_price)
            print ("Selling " + str(number_stocks_held) + " stocks of " + ticker + " at a limit price of " + str(limit_order_price))
            
    #Print Confirmation
    print ("\nConfirmation")


# In[ ]:


#Woo hoo

