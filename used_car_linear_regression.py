import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error

filepath = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/automobileEDA.csv"
df = pd.read_csv(filepath)
print(df.info())
# Linear Regression
# Lets make a linear regression model for price as our target and highway mpg as our predictior value

lm = LinearRegression()
x = df[["highway-mpg"]]
y = df["price"]

lm.fit(x, y)
yhat = lm.predict(x)
print(yhat[0:5])

print("Intercept of highway mpg model: ", lm.intercept_)
print("Slope of highway mpg model: ", lm.coef_)
print(f"Final estimated linear model: {lm.intercept_} + {lm.coef_} * highway-mpg")

# Lets make a linear regression model for price as our target and engine size as our predictior value

lm1 = LinearRegression()
x = df[["engine-size"]]
y = df["price"]

lm1.fit(x, y)
yhat = lm1.predict(x)
print(yhat[0:5])

print("Intercept of engine size model: ", lm1.intercept_)
print("Slope of engine size model: ", lm1.coef_)
print(f"Final estimated linear model: {lm1.intercept_} + {lm1.coef_} * engine-size")

# Multiple Linear Regression
# From previous eda we know that, horsepower, curb weight, engine size and highwway mpg are good predictors of price

Z = df[["horsepower", "curb-weight", "engine-size", "highway-mpg"]]

lm.fit(Z, df['price'])
yhat = lm.predict(Z)
print(yhat[0:5])

print(f"Final estimated linear model: {lm.intercept_} + {lm.coef_[0]} * {Z.columns[0]} + {lm.coef_[1]} * {Z.columns[1]} + {lm.coef_[2]} * {Z.columns[2]} + {lm.coef_[3]} * {Z.columns[3]}")

# Create and train a Multiple Linear Regression model "lm2" where the response variable is "price", and the predictor variable is "normalized-losses" and "highway-mpg".
lm2 = LinearRegression()
lm2.fit(df[["normalized-losses", "highway-mpg"]], df["price"])
print(f"Cofficient: {lm2.coef_}")

# Lets visualize simple linear regression
sns.regplot(x="highway-mpg", y="price", data=df)
plt.ylim(0,)
plt.show()

sns.regplot(x="peak-rpm", y="price", data = df)
plt.ylim(0,)
plt.show()

# From looking at the plots highway mpg is more strongly related to the price, lets verify by looking at the numerical value
print(f"Highway mpg correlatiion: {df[["highway-mpg", "price"]].corr()}")
print(f"Peak rpm correlatiion: {df[["peak-rpm", "price"]].corr()}")
# Corr verifies our judgement

# Residual Plot for simple linear regression. residual is bascially the difference between the observed value and the predicted value
sns.residplot(x=df["highway-mpg"], y=df["price"])
plt.show()

# Multiple Linear Regression plotting
# One way to look at the fit of the model is by looking at the distribution plot. We can look at the distribution of the fitted values that result from the model and compare it to the distribution of the actual values.

yhat = lm.predict(Z)

plt.figure(figsize=(12,8))
ax1 = sns.kdeplot(df["price"], color="r", fill=True, label="Actual Value")
sns.kdeplot(yhat, color="b", label="Predicted Value", fill=True, ax=ax1)
plt.xlabel("Price (US Dollars)")
plt.ylabel("Proportion of Cars")
plt.show()
plt.close()

# Polynomial Regression
# First well create a function to plot the polynomial data

def polyPlot(model, indepedent_var, dependent_var, name):
    x_new = np.linspace(15,55,100)
    y_new = model(x_new)

    plt.plot(indepedent_var, dependent_var, '.', x_new, y_new, '-')
    plt.title(f"Polynomial fit with Matplotlib for Price wrt {name}")
    ax = plt.gca()
    ax.set_facecolor((0.900, 0.900, 0.900))
    
    plt.xlabel(name)
    plt.ylabel("Price of Cars")
    plt.show()
    plt.close()

lm = LinearRegression()
x = df["highway-mpg"]
y = df["price"]

f = np.polyfit(x, y, 3)
p = np.poly1d(f)

polyPlot(p, x, y, "highway-mpg")


# Multivariate Polynomial Regression

Z = df[["horsepower", "curb-weight", "engine-size", "highway-mpg"]]
y = df["price"]

poly = PolynomialFeatures(degree=2)
Z_poly = poly.fit_transform(Z)
print(Z.shape)
print(Z_poly)

# Pipeline
# Data Pipelines simplify the steps of processing the data. We use the module Pipeline to create a pipeline. We also use StandardScaler as a step in our pipeline.
Input = [('scale',StandardScaler()),('polynomial',PolynomialFeatures(degree=2, include_bias=False)),('model', LinearRegression())]
pipe = Pipeline(Input)

Z = Z.astype(float)
pipe.fit(Z,y)

ypipe = pipe.predict(Z)
print(ypipe[0:4])

# Lets check the R^2 value
print("R squared value: ", pipe.score(Z, y))

# Lets get the MSE
mse = mean_squared_error(y, ypipe)
print("Mean squared error:", mse)

# Lets check our model with new values for the predictor values
lm = LinearRegression()
x = df[["engine-size"]]
y = df["price"]
lm.fit(x,y)
x_new = np.random.randn(100,1)
yhat = lm.predict(x_new)
print("For new test results:", yhat[0:5])