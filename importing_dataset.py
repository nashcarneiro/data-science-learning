import pandas as pd
import requests
import numpy as np

url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/auto.csv'

df = pd.read_csv(url)

print("First 5 lines of the dataset:\n")
print(df.head())

print("\nLast 10 lines of the dataset:\n")
print(df.tail(10))

headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]
print("\nheaders\n", headers)

df.columns=headers

print("First 5 rows of updated dataset:\n")
print(df.head())

print("Last 5 rows in updated dataset:\n")
print(df.tail(5))

#Now, we need to replace the "?" symbol with NaN so the dropna() can remove the missing values:
df1=df.replace("?",np.nan)

#You can drop missing values along the column "price" as follows:
df = df1.dropna(subset=["price"], axis=0)
print(df.head(20))

#saving the dataset
df.to_csv("automobile.csv", index=False)

print(df.dtypes)

print(df[["length","compression-ratio"]].describe())

print(df.info())



