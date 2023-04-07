import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error
import yfinance as yf

def download_stock_data(ticker, start_date, end_date):
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data


ticker = 'AAPL'
start_date = '2015-01-01'
end_date = '2021-01-01'
data = download_stock_data(ticker, start_date, end_date)

data['Close'] = data['Adj Close']
data = data[['Close']]

plt.figure(figsize=(10, 6))
plt.plot(data['Close'])
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.title('Apple Stock Price Time Series')
plt.show()

train_data = data['Close'][:int(len(data)*0.8)]
test_data = data['Close'][int(len(data)*0.8):]

model = ARIMA(train_data, order=(1, 1, 1))
model_fit = model.fit()

forecast = model_fit.forecast(steps=len(test_data))
mse = mean_squared_error(test_data, forecast)
print("Mean Squared Error:", mse)

plt.figure(figsize=(10, 6))
plt.plot(train_data, label='Training Data')
plt.plot(test_data, label='Test Data')
plt.plot(test_data.index, forecast, label='Forecast', color='r')
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.title('ARIMA Model Forecast')
plt.legend()
plt.show()