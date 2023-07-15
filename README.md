# Linear Regression Model for Predictive Analysis

This Python code demonstrates the implementation of a linear regression model for predictive analysis using the scikit-learn library. The code performs the following steps:

1. **Loads the data:** The code reads the data from a CSV file called "mydata.csv" using the Pandas library.

2. **Exploratory Analysis:** Provides information about the dataset, such as the number of instances and predictors. It also displays the correlation matrix of the predictors.

3. **Data Preparation:** Separates the predictors (features) and the target variable (y) from the dataset.

4. **Data Split:** Splits the data into training and testing sets using the `train_test_split` function from scikit-learn.

5. **Linear Regression Model:** Creates an instance of the `LinearRegression` class and trains the model using the training data.

6. **Model Evaluation:** Predicts the target variable for the test data and evaluates the model's performance using Mean Squared Error (MSE), Root Mean Squared Error (RMSE), and R-squared metrics.

## Dependencies
- pandas
- scikit-learn

## Usage
1. Ensure that you have the necessary dependencies installed.
2. Provide your dataset in CSV format and update the file path in the code: `data = pd.read_csv("mydata.csv")`.
3. Modify the list of predictor variables (`v1`, `v2`, `v3`, etc.) to match the column names in your dataset.
4. Run the code and observe the model evaluation metrics.
5. Feel free to customize the code according to your specific dataset and requirements.
