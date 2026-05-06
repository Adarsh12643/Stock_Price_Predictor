# Stock Price Predictor

This project demonstrates a basic machine learning workflow to analyze and predict stock price trends using Python. It uses historical data from Yahoo Finance to train a Linear Regression model that predicts stock closing prices based on time.

## 🚀 Overview
The script performs the following steps:
1. **Data Acquisition**: Downloads historical stock data using the `yfinance` API.
2. **Preprocessing**: Converts dates into ordinal format for compatibility with Scikit-Learn models.
3. **Modeling**: Implements a `LinearRegression` model to find the line of best fit for the price trend.
4. **Evaluation**: Calculates the Mean Squared Error (MSE) to quantify prediction accuracy.
5. **Visualization**: Generates a Matplotlib chart comparing actual prices against the predicted linear trend.

## 🛠️ Requirements

You will need Python 3.x installed along with the following libraries:

```bash
pip install yfinance pandas numpy matplotlib scikit-learn
```

## 📈 Usage

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Adarsh12643/stock-linear-regression.git
   ```
2. **Navigate to the directory:**
   ```bash
   cd stock-linear-regression
   ```
3. **Run the script:**
   ```bash
   python stock_prediction.py
   ```

## 📊 Sample Output
The model outputs a Mean Squared Error (MSE) value and a visualization. A lower MSE indicates the linear trend is more closely aligned with historical data.

> **Note:** Because stock markets are highly volatile and non-linear, this model is intended to show long-term trends rather than provide day-to-day trading signals.

## ⚠️ Disclaimer
This project is for educational purposes only. Stock market investments carry inherent risks. Linear regression is a simplistic model that does not account for market sentiment, news, or complex economic factors. Never use this code as the sole basis for financial decisions.

## 📝 License
Distributed under the MIT License. See `LICENSE` for more information.
