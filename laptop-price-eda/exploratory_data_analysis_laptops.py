import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats



URL="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-Coursera/laptop_pricing_dataset_mod2.csv"
df = pd.read_csv(URL, index_col=[0,1])

# Generate regression plots for each of the parameters "CPU_frequency", "Screen_Size_inch" and "Weight_pounds" against "Price". Also, print the value of correlation of each feature with "Price".

sns.regplot(x="CPU_frequency", y="Price", data=df)
plt.ylim(0,)
plt.show()

print(f"Correlation between CPU frequency and price:{df[["CPU_frequency","Price"]].corr()}")

sns.regplot(x="Screen_Size_inch", y="Price", data = df)
plt.ylim(0,)
plt.show()

print(f"Correlation between screen size and price:{df[["Screen_Size_inch", "Price"]].corr()}")

sns.regplot(x="Weight_pounds", y="Price", data = df)
plt.ylim(0,)
plt.show()

print(f"Correlation beteen weight and price: {df[["Weight_pounds", "Price"]].corr()}")

# Interpretation : CPU Frequency has a 36% positive correlation with the price, the other two features have weak correlation

# Now generate Box plots for the different feature that hold categorical values. These features would be "Category", "GPU", "OS", "CPU_core", "RAM_GB", "Storage_GB_SSD"

sns.boxplot(x="Category", y="Price", data = df)
plt.show()
sns.boxplot(x="GPU", y="Price", data = df)
plt.show()
sns.boxplot(x="OS", y="Price", data= df)
plt.show()
sns.boxplot(x="CPU_core", y="Price", data = df)
plt.show()
sns.boxplot(x="RAM_GB", y="Price", data = df)
plt.show()
sns.boxplot(x="Storage_GB_SSD", y="Price", data= df)
plt.show()

# Boxplot analysis shows noticeable differences in median  and interquartile prices of each feature across their respective categories suggesting that they can be informative predictors in future machine learning models

# Generate the statistical description of all the features being used in the data set. Include "object" data types as well.
print(df.describe(include='all'))

# Group the parameters "GPU", "CPU_core" and "Price" to make a pivot table and visualize this connection using the pcolor plot.

group1 = df[["GPU", "CPU_core", "Price"]]
grouped1 = group1.groupby(["GPU", "CPU_core"], as_index=False).mean()
print(grouped1)

pivot1 = grouped1.pivot(index="GPU", columns="CPU_core")
print(pivot1)

fig, ax = plt.subplots()
im = ax.pcolor(pivot1, cmap="RdBu")

xlabel = pivot1.columns.levels[1]
ylabel = pivot1.index

ax.set_xticks(np.arange(pivot1.shape[1]) + 0.5, minor=False)
ax.set_yticks(np.arange(pivot1.shape[0]) + 0.5, minor=False)

ax.set_xticklabels(xlabel, minor=False)
ax.set_yticklabels(ylabel, minor=False)

ax.set_xlabel("CPU_core")
ax.set_ylabel("GPU")

fig.colorbar(im)
plt.show()

# Using pearsons coefficient on all the categories

categories = ['RAM_GB','CPU_frequency','Storage_GB_SSD','Screen_Size_inch','Weight_pounds','CPU_core','OS','GPU','Category']

for category in categories:
    pearson_coef, p_value = stats.pearsonr(df[category], df['Price'])
    print(category)
    print(f"The Pearson Coefficient value of {category} is {pearson_coef:.3f} and the p-value is {p_value:.20f}")


# Inference: Pearson Coefficient analysis showed that the RAM_GB (r=0.549) and the CPU_core (r=0.459) show moderate positive correlation with Price. Whereas all the other categories showed weak corelation with Price

