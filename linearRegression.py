import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

# First lets create the random data
np.random.seed(42)
x = np.random.rand(100) * 10
y = 3 * x + np.random.normal(0,3,100)
data = pd.DataFrame({
    'X': x,
    'Y': y
})

print(data.head(10))


# Splitting our data in test and train data... 20% test data 
x_train, x_test, y_train, y_test = train_test_split(data[["X"]], data["Y"], test_size=0.2, random_state=42)

#  Create the model
model = LinearRegression()

# Train the model
model.fit(x_train, y_train)

# Get the predicted values
yhat = model.predict(x_test)

# Lets check the mean absolute error
mae = mean_absolute_error(y_test, yhat)
print(f"Mean Absolute Error: {mae}")

# Lets visualize the difference beween the true and predicted values using KDE (Kernel Density Estimate)... If the model is good then red line (the predicted values) should closely overlap the blue line (actual values)
plt.figure(figsize=(8,5))

sns.kdeplot(
    y_test,
    label = "True Values",
    fill=True,
    color="blue"
)

sns.kdeplot(
    yhat,
    label = "Predicted Values",
    fill=True,
    color="red"
)

plt.xlabel("Target Variable")
plt.ylabel("Density")
plt.title("KDE Plot of Actual Values vs Predicted Values")

plt.legend()
plt.show()


