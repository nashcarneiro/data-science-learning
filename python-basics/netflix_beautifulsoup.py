import pandas as pd
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as py

#Basically here were going to send a request to get an html file and then parse it using beautiful soup and access its content

URL = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/netflix_data_webpage.html"

data = requests.get(URL).text

soup = BeautifulSoup(data, 'html.parser')

netflix_data = pd.DataFrame(columns=['Date','Open','High','Low','Close','Adj Close','Volume'])

#from the IBM course i know the location of this data and well use find and find all methods to search for the same.

for row in soup.find("tbody").find_all("tr"):
    col = row.find_all("td")
    date = col[0].text
    open = col[1].text
    high = col[2].text
    low = col[3].text
    close = col[4].text
    adj_close = col[5].text
    volume = col[6].text
    
    new_data = pd.DataFrame({"Date":[date],"Open":[open],"High":[high],"Low":[low],"Close":[close],"Adj Close":[adj_close],"Volume":[volume]})

    netflix_data = pd.concat([netflix_data,new_data],ignore_index=True)

print(netflix_data.head())

netflix_data["Open"] = pd.to_numeric(netflix_data["Open"])

netflix_data.plot(x="Date", y="Open")
py.show()

