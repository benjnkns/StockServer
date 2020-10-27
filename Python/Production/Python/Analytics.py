#!/usr/bin/env python
# coding: utf-8

# In[1]:


def Simple_Moving_Average (closing_prices):
    SMA = []
    for i in range (0,10):
        SMA.append(0)
    for i in range (10, len(closing_prices)):
        SMA.append(sum(closing_prices[i-10:i])/10)
    
    return SMA


# In[9]:


def Simple_Moving_Average_20Day (closing_prices):
    SMA20 = []
    for i in range (0,20):
        SMA20.append(0)
    for i in range (20, len(closing_prices)):
        SMA20.append(sum(closing_prices[i-20:i])/20)

    return SMA20


# In[3]:


def Relative_Strength_Index (closing_prices):
    RSI = []
    avg_gain = []
    avg_loss = []
    gains = []
    losses = []
    
    for i in range (14, len(closing_prices)):
        for j in range(i-14, i):
            if closing_prices[j+1]>closing_prices[j]:
                gains.append(closing_prices[j+1] - closing_prices[j])
            else:
                losses.append(closing_prices[j] - closing_prices[j+1])
        avg_gain.append(sum(gains)/len(gains))
        avg_loss.append(sum(losses)/len(losses))
        gains = []
        losses = []

    for i in range (0,14):
        RSI.append(0)
    for i in range (0, len(closing_prices)-14):
        RSI.append (100 - (100 / (1 + avg_gain[i] / avg_loss[i])))

        
        
    return RSI


# In[4]:


def Standard_Deviation (closing_prices):
    STD = []
    for i in range (0,10):
        STD.append(0)
    for i in range (10, len(closing_prices)):
        STD.append(closing_prices[i-10:i].std() * 10)
        
    return STD


# In[8]:


def Bandwidth (closing_prices, STD):
    BW = []
    upper_band = []
    lower_band = []

    for i in range (0, len(closing_prices)):
        upper_band.append(closing_prices[i]+.5*STD[i])
        lower_band.append(closing_prices[i]-.5*STD[i])
        BW.append(upper_band[i] - lower_band[i])

        
    return BW


# In[6]:


def Rate_Of_Change (closing_prices):
    ROCP = []
    for i in range (0, 10):
        ROCP.append(0)
    for i in range (10, len(closing_prices)):
        ROCP.append(closing_prices[i] / closing_prices[i-10] - 1)
        
        
    return ROCP


# In[7]:


def Rate_Of_Change_20Day (closing_prices):
    ROCP100 = []
    for i in range (0, 10):
        ROCP100.append(0)
    for i in range (10, len(closing_prices)):
        ROCP100.append(closing_prices[i] / closing_prices[i-10] * 100)

    
    return ROCP100


# In[ ]:




