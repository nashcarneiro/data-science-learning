import pandas as pd
import yfinance as yf
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt


def make_graph(stock_data, revenue_data, stock):
    stock_data_specific = stock_data[stock_data.Date <= '21-06-14']
    revenue_data_specific = revenue_data[revenue_data.Date <= '21-04-30']

    fig, axes = plt.subplots(2, 1, figsize=(12,8), sharex=True)
    
    axes[0].plot(pd.to_datetime(stock_data_specific.Date), stock_data_specific.Close.astype("float"), label="Share Price", color="blue")
    axes[0].set_ylabel("Price (US$)")
    axes[0].set_title(f"{stock} Historical Share Price")

    axes[1].plot(pd.to_datetime(revenue_data_specific.Date), revenue_data_specific.Revenue.astype("float"), label="Revenue", color="green")
    axes[1].set_ylabel("Revenue (US$ Millions)")
    axes[1].set_xlabel("Date")
    axes[1].set_title(f"{stock} Historical Revenue")

    plt.tight_layout()
    plt.show()


tesla = yf.Ticker("TSLA")
tesla_data = tesla.history(period="max")
tesla_data.reset_index(inplace=True)

print(tesla_data.head())

URL = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"
data = requests.get(URL).text
soup = BeautifulSoup(data, "html.parser")

revenue = []

tables = soup.find_all("table")

for table in tables:
    headers = table.find_all("th")

    for head in headers:
        if "Tesla Quarterly Revenue" in head:
            quarterly_table = table
            break

for row in quarterly_table.find("tbody").find_all("tr"):
    cols = row.find_all("td")
    
    revenue.append({
        "Date": cols[0].text.strip(),
        "Revenue": cols[1].text.strip()
    })

tesla_revenue = pd.DataFrame(revenue)

tesla_revenue["Revenue"] = tesla_revenue['Revenue'].str.replace(r',|\$',"",regex=True)

tesla_revenue.dropna(inplace=True)
tesla_revenue = tesla_revenue[tesla_revenue['Revenue']!=""]

print(tesla_revenue.tail())


gme = yf.Ticker("GME")
gme_data = gme.history(period="max")
gme_data.reset_index(inplace=True)

print(gme_data.head())

URL = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html"
data = requests.get(URL).text
soup = BeautifulSoup(data, "html.parser")

revenue = []

tables = soup.find_all("table")

for table in tables:
    headers = table.find_all("th")
     
    for header in headers:
        if "GameStop Quarterly Revenue" in head:
            quarterly_table = table
            break

for row in quarterly_table.find("tbody").find_all("tr"):
    cols = row.find_all("td")

    revenue.append({
        "Date":cols[0].text.strip(),
        "Revenue":cols[1].text.strip()
    })

gme_revenue = pd.DataFrame(revenue)

gme_revenue["Revenue"] = gme_revenue['Revenue'].str.replace(r',|\$',"",regex=True)

gme_revenue.dropna(inplace=True)
gme_revenue = gme_revenue[gme_revenue['Revenue']!=""]

print(gme_revenue.tail())

make_graph(tesla_data, tesla_revenue, "Tesla")
make_graph(gme_data, gme_revenue, "GameStop")
