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

## Demo

## Dataset Information
- Number of instances: 1000
- Number of predictors: 7
- Target variable: y

## Exploratory Analysis
Correlation matrix:
|       |      y |      v1 |      v2 |      v3 |      v4 |      v5 |      v6 |      v7 |
|------:|-------:|--------:|--------:|--------:|--------:|--------:|--------:|--------:|
|     y | 1.0000 | -0.0114 | -0.2334 |  0.4103 | -0.0972 | -0.0270 |  0.0351 |  0.1508 |
|    v1 | -0.0114 |  1.0000 | -0.0154 | -0.0066 | -0.0319 |  0.0559 |  0.0240 |  0.0201 |
|    v2 | -0.2334 | -0.0154 |  1.0000 | -0.1231 | -0.0113 |  0.0470 | -0.0051 | -0.0350 |
|    v3 |  0.4103 | -0.0066 | -0.1231 |  1.0000 | -0.0283 | -0.0100 |  0.0361 |  0.0905 |
|    v4 | -0.0972 | -0.0319 | -0.0113 | -0.0283 |  1.0000 |  0.0430 |  0.0355 |  0.0140 |
|    v5 | -0.0270 |  0.0559 |  0.0470 | -0.0100 |  0.0430 |  1.0000 | -0.0276 | -0.0380 |
|    v6 |  0.0351 |  0.0240 | -0.0051 |  0.0361 |  0.0355 | -0.0276 |  1.0000 | -0.0377 |
|    v7 |  0.1508 |  0.0201 | -0.0350 |  0.0905 |  0.0140 | -0.0380 | -0.0377 |  1.0000 |

## Model Evaluation
- Mean Squared Error (MSE): 0.11334201041459455
- Root Mean Squared Error (RMSE): 0.3366630517514426
- R-squared: 0.17733979013177625
