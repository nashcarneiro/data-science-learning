import pandas as pd
import numpy as np

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-Coursera/laptop_pricing_dataset_base.csv"
laptop_data = pd.read_csv(url, header=None)

print(laptop_data.head())

headers = ["Manafacturer","Category","Screen","GPU","OS","CPU_core","Screen_Size_inch","CPU_frequency","RAM_GB","Storage_GB_SSD","Weight_kg","Price"]
laptop_data.columns = headers
print(laptop_data.head())

laptop_data.replace("?", np.nan, inplace=True)

laptop_data.to_csv("laptop_pricing.csv", index=False)

print(laptop_data.dtypes)
print(laptop_data.describe(include="all"))
print(laptop_data.info())