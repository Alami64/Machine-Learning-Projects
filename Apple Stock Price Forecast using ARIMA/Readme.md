# Apple Stock Price Forecast using ARIMA
This repository contains a Python script that forecasts Apple's stock price using the ARIMA (AutoRegressive Integrated Moving Average) model.

## Dependencies
The following Python libraries are required to run the code:

- pandas
- numpy
- matplotlib
- statsmodels
- scikit-learn
- yfinance

You can install these dependencies using the following command:
```python
pip install pandas numpy matplotlib statsmodels scikit-learn yfinance
```
## Usage
The script stock_forecast_arima.py downloads historical stock data for Apple Inc. (AAPL) from Yahoo Finance, and then fits an ARIMA model to forecast the stock price.
1. Download or clone this repository to your local machine.
2.  Navigate to the repository folder in your terminal or command prompt.
3. Run the script using the following command:
```python
python stock_forecast_arima.py
```
The script will output two plots:

1. Apple Stock Price Time Series: This plot displays the historical stock prices of Apple Inc.
2. ARIMA Model Forecast: This plot shows the ARIMA model's prediction of the stock price compared to the actual stock price.

Additionally, the script will print the Mean Squared Error (MSE) of the ARIMA model's forecast.

## Customization
You can modify the script to forecast stock prices for other companies by changing the ticker variable in the script. For example, to forecast the stock price of Microsoft (MSFT), change the following line:
```python
ticker = 'AAPL'
```
to

```python
ticker = 'MSFT'
```
You can also adjust the date range for the historical stock data by changing the start_date and end_date variables.
