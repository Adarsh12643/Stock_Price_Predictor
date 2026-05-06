import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# 1. Download Historical Data
# We'll use Google (GOOGL) as an example
ticker = "GOOGL"
data = yf.download(ticker, start="2020-01-01", end="2024-01-01")

# 2. Data Preprocessing
# We want to predict the 'Close' price based on the day number
data['Date_Ordinal'] = pd.to_datetime(data.index).map(pd.Timestamp.toordinal)

X = data[['Date_Ordinal']] # Independent variable
y = data['Close']          # Dependent variable

# 3. Split the data into Training and Testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Initialize and Train the Linear Regression Model
model = LinearRegression()
model.fit(X_train, y_train)

# 5. Make Predictions
predictions = model.predict(X_test)

# 6. Evaluate the Model
mse = mean_squared_error(y_test, predictions)
print(f"Mean Squared Error: {mse:.2f}")

# 7. Visualization
plt.figure(figsize=(12, 6))
plt.scatter(X_test, y_test, color='blue', label='Actual Price', s=10)
plt.plot(X_test, predictions, color='red', linewidth=2, label='Predicted Trend (Linear Regression)')
plt.title(f'{ticker} Stock Price Prediction')
plt.xlabel('Date (Ordinal)')
plt.ylabel('Price (USD)')
plt.legend()
plt.show()