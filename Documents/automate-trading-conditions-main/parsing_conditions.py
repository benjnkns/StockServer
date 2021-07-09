#!/usr/bin/env python
# coding: utf-8


from pyparsing import *
import pydash
import pandas as pd
from credentials import ROBIN_USER_NAME, ROBIN_PWD
from pydash import at
from finviz.screener import Screener
import finviz


# In[3]:


def parse_overall_logic(logic_condition):
    
    condition_start = Keyword("if")

    result = Keyword("then")

    final = Keyword("else")

    condition_end = Word(alphanums + "._,()[]=><!$#-") | quotedString

    value =  Word(alphanums + "-._,()[]=><!$#") | quotedString

    grammar = (condition_start.suppress() + Group(OneOrMore(condition_end, stopOn=result).setParseAction(" ".join) +                 result.suppress() + value )) + Group(final +value) 
    
    parsed_string = grammar.parseString(logic_condition)
    
    parse_initial_ticker_cdt = list(parse_inital_ticker(parsed_string[0][0])[0])
    parse_trade_logic_cdt = list(parse_trade_logic(parsed_string[0][1])[0])

    
    return (parse_initial_ticker_cdt, parse_trade_logic_cdt)


# In[4]:


def parse_inital_ticker(initial_condition):
    begin = Word("#")
    ticker = Word(alphanums)
    mid = Word("<>=")
    end = Word(nums+'-')
    
    return Group(begin+ticker+mid+end).parseString(initial_condition)


# In[5]:


def parse_trade_logic(condition):
    
    begin = (Keyword("buy") | Keyword("sell"))
    
    return Group(Literal("'") +begin + (Literal("$") | Literal('@')) + Word(nums)).parseString(condition)


# In[7]:


pydash.flatten(parse_overall_logic("if #tsla < -5 then 'buy $500' else 0"))


# In[31]:


def parse_all_conditions():
    
    conditions_df = pd.read_csv('conditions.csv')
    
    parsed_conditions = []

    for item in conditions_df.iterrows():
        category = item[1][0]
        condition_str = item[1][1]

        parsed_conditions.append(pydash.flatten(parse_overall_logic(condition_str)))
    
    conditions_df['parsed_conditions'] = parsed_conditions
    
    all_tickers = []

    for parsed_condition in parsed_conditions:

        if parsed_condition[0] != '#':
            print("Issue with ticker. Use upper case!")
        if parsed_condition[2] not in ['<','>','=']:
            print("Condition not regoginized")
        if not parsed_condition[3].isnumeric() and not parsed_condition[7].isnumeric() :
            print("stock condition number not regoginized ")

        if parsed_condition[5].lower() not in ['buy','sell'] :
            print("Buy or sell not regoginzed ")
        if parsed_condition[6] not in ['$','@'] :
            print("amount symbol not regonized")

        all_tickers.append(parsed_condition[1])
        
        
    return conditions_df


# In[ ]:



def can_buy(profile, amount, type ="stocks"):

    buying_power = float(profile['buying_power'])
    margin_cash = float(profile['margin_balances']['unallocated_margin_cash'])
    crypto_cash = float(profile['crypto_buying_power'])


    if type =="stocks" and buying_power >= amount and margin_cash >= amount:
        return True
    elif type =="crypto" and crypto_cash >= amount:
        return True
    else:
        return False


# In[32]:


def perform_buy_sell(conditions_df):
    
    #stock_positions = get_robinhood_positions(lagging = True)

    #profile = r.profiles.load_account_profile()

    
    for condition in conditions_df.iterrows():

        category = condition[1][0]
        parsed_condition = condition[1][2]

        print(parsed_condition)

        ticker_price = str(float((at(finviz.get_stock(parsed_condition[1]),'Price')[0])))

        ticker_pct = str(float((at(finviz.get_stock(parsed_condition[1]),'Change')[0]).split('%')[0]))

        condition_price_str = "1 if "+ticker_price+' '+parsed_condition[2]+' '+parsed_condition[3]+" else 0"
        condition_pct_str = "1 if "+ticker_pct+' '+parsed_condition[2]+' '+parsed_condition[3]+" else 0"

        if category =='price':


            if eval(condition_price_str) ==1                    and parsed_condition[5] =='buy':

                #r.orders.order_buy_fractional_by_price(symbol = parsed_condition[1], amountInDollars=parsed_condition[-1])

                #Use your brokerage API to buy here
                print(f"Buying {parsed_condition[-1]} of {parsed_condition[1]}" )

            # If you are okay, with short sell, you do not have to even hold the stock
            elif eval(condition_price_str) ==1                    and parsed_condition[5] =='sell':

                #Use your brokerage API to sell here
                print(f"Selling {parsed_condition[-1]} of {parsed_condition[1]}" )

        elif category =='pct':

            if eval(condition_pct_str) ==1                    and parsed_condition[5] =='buy':
                
                #Use your brokerage API to buy here
                #r.orders.order(symbol = parsed_condition[1],side=parsed_condition[5], quantity=parsed_condition[-1])
                print(f"Buying {parsed_condition[-1]} of {parsed_condition[1]}" )

            elif eval(condition_pct_str) ==1                    and parsed_condition[5] =='sell':

                #Use your brokerage API to sell here

                print(f"Selling {parsed_condition[-1]} of {parsed_condition[1]}" )
# In[33]:

if __name__=='__main__':
    conditions_df = parse_all_conditions()


# In[34]:



perform_buy_sell(conditions_df)

