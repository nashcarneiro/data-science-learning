import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy import stats

file_path= "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/automobileEDA.csv"
df = pd.read_csv(file_path)
print(df.head())
print(df.info())

stroke_mode = (df["stroke"].mode()[0])
df["stroke"] = df["stroke"].fillna(stroke_mode)
print(df.isnull().sum())

# we can calculate the correlation between variables of type "int64" or "float64" using the method "corr"

numeric_data = df.select_dtypes(include=["float64", "int64"])
print(numeric_data.corr())

# Find the correlation between the following columns: bore, stroke, compression-ratio, and horsepower.

cols = ['bore','stroke','compression-ratio', 'horsepower']
print(df[cols].corr())

# In order to start understanding the (linear) relationship between an individual variable and the price, we can use "regplot"
# which plots the scatterplot plus the fitted regression line for the data. 

sns.regplot(x="engine-size", y="price", data=df)
plt.ylim(0,)
plt.show()

#engine price shows a strong positive correlation with the price... hence its a good indicator of price... when the engine size gets larger the price goes up

print("Correlation between engine size and price:")
print(df[["engine-size", "price"]].corr())

#lets check the relation between highway mpg and price using regplot

sns.regplot(x="highway-mpg", y="price", data=df)
plt.ylim(0,)
plt.show()

#highway mgp shows a negative correlation with the price... hences its a good indicator of price.. when the highway mpg goes up the price goes down
print("Correlation between highway mpg and price:")
print(df[["highway-mpg", "price"]].corr())

#Lets see if peal rpm is a predictor variable of price

sns.regplot(x="peak-rpm", y="price", data=df)
plt.ylim(0,)
plt.show()

#the regression line appears to be pretty much horizontal making it have a neutral relationship, making it not a very good indicator of price..
print("Correlation between peak-rpm and price")
print(df[["peak-rpm","price"]].corr())


# this time lets first check correlation between stroke and price...
print("Correlation between stroke and price")
print(df[["stroke", "price"]].corr())

sns.regplot(x="stroke", y="price", data= df)
plt.ylim(0,)
plt.show()

#this again shows a weak or neutral relation



#now lets visualize categorical values using boxplots

sns.boxplot(x="body-style", y="price", data=df)
plt.show()

# We see that the distributions of price between the different body-style categories have a significant overlap, so body-style would not be a good predictor of price. Let's examine engine "engine-location" and "price

sns.boxplot(x="engine-location", y="price", data=df)
plt.show()

# Here we see that the distribution of price between these two engine-location categories, front and rear, are distinct enough to take engine-location as a potential good predictor of price.

sns.boxplot(x="drive-wheels", y="price", data=df)
plt.show()

# Here we see that the distribution of price between the different drive-wheels categories differs. As such, drive-wheels could potentially be a predictor of price.

#Value counts is a good way of understanding how many units of each characteristic/variable we have. We can apply the "value_counts" method on the column "drive-wheels". 

drive_wheel_counts = df["drive-wheels"].value_counts().to_frame()
drive_wheel_counts.reset_index(inplace=True)
print(drive_wheel_counts)

engine_location_counts = df["engine-location"].value_counts().to_frame()
engine_location_counts.reset_index(inplace=True)
print(engine_location_counts)

# After examining the value counts of the engine location, we see that engine location would not be a good predictor variable for the price. This is because we only have three cars with a rear engine and 198 with an engine in the front, so this result is skewed. Thus, we are not able to draw any conclusions about the engine location.


# Now lets use groupby to look at the mean price of cars grouped by only the drive wheels

df_group = df[["drive-wheels", "body-style", "price"]]
df_group1 = df_group.groupby(["drive-wheels"], as_index=False).agg({'price': 'mean'})
print(df_group1)

# Now lets see the price of the cars grouped by drive wheels and the body style

df_group2 = df_group.groupby(["drive-wheels", "body-style"], as_index=False).mean()
print(df_group2)

# But this table is hard to understand, lets create a pivot table so that one variable is in the index and the other is the columns, making it visually easier to understand

pivot1 = df_group2.pivot(index="drive-wheels", columns="body-style")
pivot1 = pivot1.fillna(0)
print(pivot1)

# Now lets group by body style alone
df_group3 = df_group.groupby(["body-style"], as_index=False).agg({"price":"mean"})
print(df_group3)

#Lets visualize the pivot table using a heat map
plt.pcolor(pivot1, cmap="RdBu")
plt.colorbar()
plt.ylabel("Drive-Wheels")
plt.xlabel("Body-Style")
plt.show()

#The heatmap plots the target variable (price) proportional to colour with respect to the variables 'drive-wheel' and 'body-style' on the vertical and horizontal axis, respectively. This allows us to visualize how the price is related to 'drive-wheel' and 'body-style'.
#The default labels convey no useful information to us. Let's change that

fig, ax = plt.subplots()
im = ax.pcolor(pivot1, cmap="RdBu")
#label names
xlabel = pivot1.columns.levels[1]
ylabel = pivot1.index
#move the ticks and labels to the center
ax.set_xticks(np.arange(pivot1.shape[1]) + 0.5, minor=False)
ax.set_yticks(np.arange(pivot1.shape[0]) + 0.5, minor=False)
#insert labels
ax.set_xticklabels(xlabel, minor=False)
ax.set_yticklabels(ylabel, minor=False)
#rotate the labels because names are long
plt.xticks(rotation=90)

fig.colorbar(im)
plt.show()


#Lets do the same for groupby body style and aspiration to look at how the price compares
df_group = df[["aspiration", "body-style", "price"]]
df_group4 = df_group.groupby(["aspiration","body-style"], as_index=False).mean()
print(df_group4)
pivot2 = df_group4.pivot(index="aspiration", columns="body-style")
print(pivot2)
plt.figure(figsize=(12,8))
sns.heatmap(pivot2,cmap="RdBu",annot=True, fmt=".0f", linecolor="black")
plt.title("Average Price by Aspiration and BodyStyle")
plt.xlabel=("Aspiration")
plt.ylabel("Drive Wheels")
plt.show()


#Lets calculate the pearson value and p-value of 'wheel-base' and 'price
pearson_coef, p_value = stats.pearsonr(df['wheel-base'], df['price'])
print(f"The Pearson Coefficient is:{pearson_coef:.3f}, with a P-Value of:{p_value:.20f}")
# Since the p-value is 0.001, the correlation between wheel-base and price is statistically significant, although the linear relationship isn't extremely strong (~0.585)

# Horsepower vs. Price
peorson_coeff, p_value = stats.pearsonr(df["horsepower"], df["price"])
print(f"The Pearson Coefficient is:{pearson_coef:.3f}, with a P-Value of:{p_value:.20f}")
# Since the p-value is 0.001, the correlation between horsepower and price is statistically significant, and the linear relationship is quite strong (~0.809, close to 1).

# Length vs Price
pearson_coef, p_value = stats.pearsonr(df['length'], df['price'])
print(f"The Pearson Coefficient is:{pearson_coef:.3f}, with a P-Value of:{p_value:.20f}")
# Since the p-value is 0.001, the correlation between length and price is statistically significant, and the linear relationship is moderately strong (~0.691).
 
# Width vs Price
pearson_coef, p_value = stats.pearsonr(df['width'], df['price'])
print(f"The Pearson Coefficient is:{pearson_coef:.3f}, with a P-Value of:{p_value:.20f}")
# Since the p-value is < 0.001, the correlation between width and price is statistically significant, and the linear relationship is quite strong (~0.751).

# Curb-weight vs Price
pearson_coef, p_value = stats.pearsonr(df['curb-weight'], df['price'])
print(f"The Pearson Coefficient is:{pearson_coef:.3f}, with a P-Value of:{p_value:.20f}")
# Since the p-value is 0.001, the correlation between curb-weight and price is statistically significant, and the linear relationship is quite strong (~0.834).

# Engine-Size vs Price
pearson_coef, p_value = stats.pearsonr(df['engine-size'], df['price'])
print(f"The Pearson Coefficient is:{pearson_coef:.3f}, with a P-Value of:{p_value:.20f}")
# Since the p-value is 0.001, the correlation between engine-size and price is statistically significant, and the linear relationship is very strong (~0.872).

# Bore vs Price
pearson_coef, p_value = stats.pearsonr(df['bore'], df['price'])
print(f"The Pearson Coefficient is:{pearson_coef:.3f}, with a P-Value of:{p_value:.20f}")
# Since the p-value is 0.001, the correlation between bore and price is statistically significant, but the linear relationship is only moderate (~0.521).

# City-mpg vs Price
pearson_coef, p_value = stats.pearsonr(df['city-mpg'], df['price'])
print(f"The Pearson Coefficient is:{pearson_coef:.3f}, with a P-Value of:{p_value:.20f}")
# Since the p-value is < 0.001, the correlation between city-mpg and price is statistically significant, and the coefficient of about -0.687 shows that the relationship is negative and moderately strong.

# Highway-mpg vs Price
pearson_coef, p_value = stats.pearsonr(df['highway-mpg'], df['price'])
print(f"The Pearson Coefficient is:{pearson_coef:.3f}, with a P-Value of:{p_value:.20f}")
# Since the p-value is < 0.001, the correlation between highway-mpg and price is statistically significant, and the coefficient of about -0.705 shows that the relationship is negative and moderately strong.

# We now have a better idea of what our data looks like and which variables are important to take into account when predicting the car price.