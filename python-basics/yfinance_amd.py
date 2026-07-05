import pandas as pd
import yfinance as yf
import json
import matplotlib.pyplot as plt

#Now using the Ticker module create an object for AMD (Advanced Micro Devices) with the ticker symbol is AMD called; name the object amd

amd = yf.Ticker("AMD")
amd_info = amd.info

with open("amd.json", "w") as file:
    json.dump(amd_info, file)

with open("amd.json") as file:
    data = json.load(file)

    #Question 1 Use the key 'country' to find the country the stock belongs to.
    print(data["country"])

    #Question 2 Use the key 'sector' to find the sector the stock belongs to.
    print(data["sector"])

    #Question 3 Obtain stock data for AMD using the history function, set the period to max. 
    # Find the Volume traded on the first day (first row).

    amd_share_price = amd.history(period= "ytd")
    amd_share_price.reset_index(inplace=True)
    print(amd_share_price.head())

    amd_share_price.plot(x="Date", y="Open")
    plt.show()

    print(amd_share_price.iloc[0]["Volume"])
    