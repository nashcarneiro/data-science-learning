# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_val_predict
from sklearn.preprocessing import PolynomialFeatures
import warnings
warnings.filterwarnings('ignore')
from tqdm import tqdm


# %%
filepath = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/module_5_auto.csv'
df = pd.read_csv(filepath, header=0)
df.drop(["Unnamed: 0.1", "Unnamed: 0"], axis = 1, inplace=True)
df=df._get_numeric_data()

# %%
print(df.head())

# %%
# Functions for plotting
def DistributionPlot(BlueFunction, RedFunction, BlueLabel, RedLabel, Title):
    plt.figure(figsize=(10,8))

    ax1 = sns.kdeplot(BlueFunction, color="b", label=BlueLabel)
    ax2 = sns.kdeplot(RedFunction, color="r", label=RedLabel, ax=ax1)

    plt.title(Title)
    plt.xlabel("Price (US$)")
    plt.ylabel("Proportion of Cars")
    plt.legend()
    plt.show()
    plt.close()

def PolyPlot(x_train, x_test, y_train, y_test, lr, poly_tranform):
    plt.figure(figsize=(10,8))

    xmax = max([x_train.max(), x_test.max()])
    xmin = min([x_train.min(), x_test.min()])

    x = np.arange(xmin, xmax, 0.1).reshape(-1,1)

    plt.plot(x_train, y_train, 'ro', label='Training data')
    plt.plot(x_test, y_test, 'go', label="Test Data")
    plt.plot(x, lr.predict(poly_tranform.fit_transform(x)), label="Predicted function")
    plt.ylim([-10000,60000])
    plt.ylabel("Price")
    plt.legend()
    plt.show()
    


# %%
y_data = df["price"]
x_data = df.drop("price", axis=1)

xtrain, xtest, ytrain, ytest, = train_test_split(x_data, y_data, test_size=0.10, random_state=1)

print("Number of training data samples: ", xtrain.shape[0])
print("Number of test samples: ", xtest.shape[0])



# %%
lr = LinearRegression()
lr.fit(xtrain[["horsepower"]], ytrain)
print(f"score for training data:  {lr.score(xtrain[['horsepower']], ytrain)}")
print(f"score for test data:  {lr.score(xtest[['horsepower']], ytest)}")


# %%
# Cross validation
# Sometimes you do not have sufficient testing data; as a result, you may want to perform cross-validation. Let's go over several methods that you can use for cross-validation.

rcross = cross_val_score(lr, x_data[["horsepower"]], y_data, cv=4)
print("R score: ", rcross)

# %%
print("average across 4 folds: ", rcross.mean()," and standard deviation is: ", rcross.std())

# %%
# R score was the default scoring metric we can change it to say for example neg_mean_sqauared_error
rcross = cross_val_score(lr, x_data[["horsepower"]], y_data, cv=4, scoring="neg_mean_squared_error")
print("MSE : ", -1 * rcross)

# %%
# We can also use cross validation to predict our data
yhat = cross_val_predict(lr, x_data[["horsepower"]], y_data, cv=4)
print(yhat[0:5])

# %%
# Overfiting and Underfiting 
# Multiple Linear Regression

lr = LinearRegression()
lr.fit(xtrain[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']], ytrain)
yhat_train = lr.predict(xtrain[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']])
print(yhat_train[0:5])

yhat_test = lr.predict(xtest[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']])
print(yhat_test[0:5])



# %%
Title = "Distribution plot of predicted value using Training data vs Training data distribution"
DistributionPlot(ytrain, yhat_train, "Actual Values (train)", "Predicted Values (train)", Title)

Title = "Distribution plot of predicted values using Test data vs Test data distribution"
DistributionPlot(ytest, yhat_test, "Actual Values (test)", "Predicted Values (test)", Title)

# %%
# We see that fig 2 has a significant drop in accuracy for the price data between $5000 and $15000
# Now lets check if polynomial regression also exhibits the same drop

xtrain, xtest, ytrain, ytest = train_test_split(x_data, y_data, test_size=0.45, random_state=0)
pf = PolynomialFeatures(degree=5)
xtrain_pr = pf.fit_transform(xtrain[["horsepower"]])
xtest_pr = pf.fit_transform(xtest[["horsepower"]])

poly = LinearRegression()
poly.fit(xtrain_pr, ytrain)
yhat = poly.predict(xtest_pr)
print("Predicted Values: ", yhat)
print("True Values: ", ytest)



# %%
PolyPlot(xtrain["horsepower"], xtest["horsepower"], ytrain, ytest, poly, pf)

# %%
print("Score of the train data is ", poly.score(xtrain_pr, ytrain))
print("Score of the test data is ", poly.score(xtest_pr, ytest))

# %%
# lets check the r score for every degree of polynomial
r2s = []
order = [1,2,3,4]
for n in order:
    pr = PolynomialFeatures(degree=n)

    xtrain_pr = pr.fit_transform(xtrain[["horsepower"]])
    xtest_pr = pr.fit_transform(xtest[["horsepower"]])

    lm = LinearRegression()

    lm.fit(xtrain_pr, ytrain)
    r2s.append(lm.score(xtest_pr, ytest))

plt.plot(order, r2s)
plt.xlabel("Order")
plt.ylabel("R^2 Score")
plt.title("R^2 score using test data for different degrees polynomials")
plt.text(3, 0.75, 'Maximum R^2 ') 
plt.show()

# %%
# The following interface allows you to experiment with different polynomial orders and different amounts of data.

def f(order, tsize):
    x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=tsize, random_state=0)
    pr = PolynomialFeatures(degree=order)
    x_train_pr = pr.fit_transform(x_train[['horsepower']])
    x_test_pr = pr.fit_transform(x_test[['horsepower']])
    poly = LinearRegression()
    poly.fit(x_train_pr,y_train)
    PolyPlot(x_train['horsepower'], x_test['horsepower'], y_train, y_test, poly,pr)

# %%
pr1 = PolynomialFeatures(degree=2)
xtrain_pr1 = pr1.fit_transform(xtrain[["horsepower", "curb-weight", "engine-size", "highway-mpg"]])
xtest_pr1 = pr1.fit_transform(xtest[["horsepower", "curb-weight", "engine-size", "highway-mpg"]])

# Now were doing polynomial fit for multiple features.. lets check the dimensions
print(xtrain_pr1.shape[1])

# %%
poly1 = LinearRegression().fit(xtrain_pr1, ytrain)
yhat_test1 = poly1.predict(xtest_pr1)
Title = "Distribution plot of Predicted value using test data vs test data distribution"
DistributionPlot(ytest, yhat_test1, "Actual values(test)", "Predicted values(test)", Title)

#The predicted value is higher than actual value for cars where the price $10,000 range, conversely the predicted price is lower than the price cost in the $30,000 to $40,000 range. As such the model is not as accurate in these ranges.


# %%
# Ridge Regression

pr = PolynomialFeatures(degree=2)
xtrain_pr = pr.fit_transform(xtrain[["horsepower", "curb-weight", "engine-size", "highway-mpg"]])
xtest_pr = pr.fit_transform(xtest[["horsepower", "curb-weight", "engine-size", "highway-mpg"]])

RidgeModel = Ridge(alpha=1)
RidgeModel.fit(xtrain_pr, ytrain)
yhat = RidgeModel.predict(xtest_pr)

print("Preicted Values:",yhat[0:5])
print("Actual Values:",ytest[0:5])


# %%
# We select the value of alpha that minimizes the test error. To do so, we can use a for loop.
# We have also created a progress bar to see how many iterations we have completed so far.

r2s_train = []
r2s_test = []
Alpha = np.array(range(0,1000))
pbar = tqdm(Alpha)

for alpha in pbar:
    RidgeModel = Ridge(alpha=alpha)
    RidgeModel.fit(xtrain_pr, ytrain)
    train_score, test_score = RidgeModel.score(xtrain_pr, ytrain), RidgeModel.score(xtest_pr, ytest)
    
    pbar.set_postfix({"Train Score":train_score, "Test Score":test_score})
    r2s_train.append(train_score)
    r2s_test.append(test_score)


# %%
plt.figure(figsize=(10,8))
plt.plot(Alpha, r2s_train, color="blue", label="Train Score")
plt.plot(Alpha, r2s_test, color="red", label="Test Score")
plt.xlabel("Alpha")
plt.ylabel("R^2 Score")
plt.legend()
plt.show()

# Inference : By looking  at the trend it appears that the r score decreases as alpha increases meaning the model performs worse as alpha increases

# %%
# Grid Search CV
#  Now to make the process of checking for the best alpha values we can use GridSearchCV

parameters = [{'alpha':[0.001, 0.1, 1, 10, 100, 1000, 10000, 100000]}]
rm = Ridge()

grid = GridSearchCV(rm, parameters, cv=4)
grid.fit(x_data[["horsepower", "curb-weight", "engine-size", "highway-mpg"]], y_data)
# Lets find the best parameters
bestp = grid.best_estimator_
print("Best alpha value for this model: ", bestp)





# %%
# Lets verify this now
rr = Ridge(alpha=0.001)
score = cross_val_score(rr, x_data[["horsepower", "curb-weight", "engine-size", "highway-mpg"]], y_data, cv=4)
print("R^2 Score for alpha:0.001 :",score.mean())
rr = Ridge(alpha=10000)
score = cross_val_score(rr, x_data[["horsepower", "curb-weight", "engine-size", "highway-mpg"]], y_data, cv=4)
print("R^2 Score for alpha:10000 :",score.mean())

# R^2 Score for alpha:0.001 : 0.6645924797281765
# R^2 Score for alpha:10000 : 0.6724916803148251
# This verifies our gridsearch


