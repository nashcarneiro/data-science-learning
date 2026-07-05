import pandas as pd
import requests
from io import StringIO

URL="https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)"

headers = {
    "User-Agent": "Mozilla/5.0"
}

html = requests.get(URL, headers=headers).text

tables = pd.read_html(StringIO(html))

df=tables[2]
df.columns = range(df.shape[1])

df=df[[0,1]]
df=df.iloc[1:11,:]
df.columns = ['Country','GDP']

df.to_excel('./gdp.xlsx', index=False)


