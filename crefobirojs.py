import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load the data
data = pd.read_csv("mydata.csv")

# Exploratory Analysis
print("Dataset Information:")
print("Number of instances:", data.shape[0])
print("Number of predictors:", data.shape[1] - 1)# Excluding the target variable
print("Target variable: y\n")

# Explore the predictors
print("Exploratory Analysis:")
correlation_matrix = data.corr()
print("Correlation matrix:")
print(correlation_matrix)

# Separate the predictors(features) and the target variable(y)
predictors = data[["v1", "v2", "v3", "v4", "v5", "v6", "v7"]]
target = data["y"]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    predictors, target, test_size = 0.2, random_state = 42
)

# Create and train the regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
rmse = mean_squared_error(y_test, y_pred, squared = False)
r2 = r2_score(y_test, y_pred)

print("\nModel Evaluation:")
print("Mean Squared Error (MSE):", mse)
print("Root Mean Squared Error (RMSE):", rmse)
print("R-squared:", r2)