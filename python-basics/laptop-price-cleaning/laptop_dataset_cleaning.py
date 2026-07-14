import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-Coursera/laptop_pricing_dataset_mod1.csv"
df = pd.read_csv(url)

print(df.info())
print(df.head())
df.drop(columns=["Unnamed: 0"], inplace=True)

#important step incase screen size and weight were a string like "Unknown". use pd.to_numeric(..., errors="coerce")
cols = ["Weight_kg", "Screen_Size_cm"]
df[cols] = df[cols].apply(pd.to_numeric, errors="coerce") 

# we can update the Screen_Size_cm column such that all values are rounded to nearest 2 decimal places by using numpy.round()

df['Screen_Size_cm']=np.round(df['Screen_Size_cm'], 2)
print(df.head())

missing = df.isnull().sum()
print(missing[missing>0])

#screen size and weight has missing values aka nan so well clean them up with mode and mean respectively

avg_weight = df["Weight_kg"].mean()
df["Weight_kg"] = df["Weight_kg"].replace(np.nan, avg_weight)

mode_screen_size = df['Screen_Size_cm'].value_counts().idxmax()
df["Screen_Size_cm"] = df['Screen_Size_cm'].fillna(mode_screen_size)

# unit conversions 
# 1 kg = 2.205 pounds
# 1 inch = 2.54 cm

df["Weight_lb"] = df["Weight_kg"]*2.205
df["Screen_Size_inch"] = df['Screen_Size_cm']/2.54

print(df.head())

# normalizing CPU_frequency

df["CPU_frequency"] = df["CPU_frequency"]/df["CPU_frequency"].max()
print(df.head())

# Create 3 bins for the attribute "Price", these bins would be named "Low", "Medium" and "High". 

bins = np.linspace(min(df["Price"]), max(df["Price"]), 4)
group_names = ["Low", "Medium", "High"]

df["Price-binned"] = pd.cut(df["Price"], bins, labels=group_names, include_lowest=True)
print(df.head())

#plotting the price-binned column on a bar graph

counts = df["Price-binned"].value_counts()
plt.bar(counts.index, counts.values)
plt.xlabel("Laptop Price")
plt.ylabel("Count")
plt.title("Laptop Price Distribution")

plt.show()

# since the screens are only full hd and ips panels lets create columns for those and drop the screen column itself
dummies = pd.get_dummies(df["Screen"])
dummies.rename(columns={'IPS Panel':'Screen-IPS Panel', 'Full HD':'Screen-Full HD'}, inplace=True)

df = pd.concat([df, dummies], axis=1)
df.drop("Screen", axis=1, inplace=True)
print(df.head())

df.to_excel("laptop_prices.xlsx", index=False)

