#You are a data scientist working for a hedge fund; it's your job to determine any suspicious stock activity. 
# In this lab you will extract stock data using a Python library. We will use the yfinance library, 
# it allows us to extract data for stocks returning data in a pandas dataframe. You will use the lab to extract.

import yfinance as yf
import pandas as pd
import json
import matplotlib.pyplot as plt

#Using the Ticker module we can create an object that will allow us to access functions to extract data. 
# To do this we need to provide the ticker symbol for the stock, here the company is Apple and the ticker symbol is AAPL.

apple = yf.Ticker("AAPL")

#Using the attribute info we can extract information about the stock as a Python dictionary.

apple_info = apple.info

with open("apple.json","w") as file:
    json.dump(apple_info, file)

with open("apple.json") as file:
    data = json.load(file)

    #A share is the single smallest part of a company's stock that you can buy, the prices of these shares fluctuate over time. 
    # Using the history() method we can get the share price of the stock over a certain period of time. Using the period parameter 
    # we can set how far back from the present to get data. The options for period are 
    # 1 day (1d), 5d, 1 month (1mo) , 3mo, 6mo, 1 year (1y), 2y, 5y, 10y, ytd, and max.

    apple_share_price = apple.history(period="max")
    apple_share_price.reset_index(inplace=True)

    print(apple_share_price.head())
    apple_share_price.plot(x="Date", y="Open")

    plt.show()

    #Dividends are the distribution of a companys profits to shareholders. In this case they are defined as an amount 
    # of money returned per share an investor owns. Using the variable dividends we can get a dataframe of the data. 
    # The period of the data is given by the period defined in the 'history` function.

    apple.dividends.plot()
    plt.show()

