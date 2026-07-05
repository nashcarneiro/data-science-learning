#As a data scientist working for a hedge fund, you will:
#Extract profit data for companies like Tesla and GameStop 
# Analyze stock price trends 
#Build a dashboard comparing stock prices and company profits


"""
Findings/Analysis:
-Tesla showed long term stock growth
-Tesla's net income increased significantly from 2021
-Game stop showed a flat line in terms of net income, but still had a spike of stock share prices in 2022-24... 
-this infers that stock prices are not only related to the companies net profitability but also to the investor sentiment and market speculation too

"""

import pandas as pd
import bs4
import yfinance as yf
import matplotlib.pyplot as plt

tesla = yf.Ticker("TSLA")
gamestop = yf.Ticker("GME")

tesla_stocks = tesla.history(period="max")
gamestop_stocks = gamestop.history(period="max")

tesla_stocks.reset_index(inplace=True)
gamestop_stocks.reset_index(inplace=True)

tesla_profit = tesla.financials.loc["Net Income"]
gamestop_profit = gamestop.financials.loc["Net Income"]

print("\nTesla stock shares:")
print(tesla_stocks.head())

print("\nGame Stop stock shares:")
print(gamestop_stocks.head())

print("\nTesla Net Income:")
print(tesla_profit)

print("\nGame Stop Net Income:")
print(gamestop_profit)

plt.plot(tesla_stocks["Date"], tesla_stocks["Open"], label="Tesla Stock Shares")
plt.plot(gamestop_stocks["Date"], gamestop_stocks["Open"], label="Game Stop Stock Shares")
plt.title("Tesla vs Game Stop Stock Share Prices")

plt.legend()
plt.show()

plt.plot(tesla_profit.index, tesla_profit.values, label="Tesla Net Income")
plt.plot(gamestop_profit.index,gamestop_profit.values, label="Game Stop Net Income")
plt.title("Tesla vs Game Stop Net Income")

plt.legend()
plt.show()

fig, ax = plt.subplots(2,1)

ax[0].plot(tesla_stocks["Date"], tesla_stocks["Open"])
ax[0].set_title("Tesla Stock Share Prices")

ax[1].plot(tesla_profit.index, tesla_profit.values)
ax[1].set_title("Tesla Net Income")

plt.show()

fig, ax = plt.subplots(2,1)

ax[0].plot(gamestop_stocks["Date"], gamestop_stocks["Open"])
ax[0].set_title("Game Stop Stock Share Prices")

ax[1].plot(gamestop_profit.index, gamestop_profit.values)
ax[1].set_title("Game Stop Net Income")

plt.show()



