import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

def get_technical_indicators_from_csv(tickers):
    data_dict = {}
    for ticker in tickers:
        try:
            data = pd.read_csv('data\\'+ticker + '.csv', index_col=0)  # Load data from CSV
            data.ffill(inplace=True)
            
            # Calculate SMA
            data['SMA'] = data['Close'].rolling(window=14).mean()
            
            # Calculate Bollinger Bands
            data['Middle_Band'] = data['Close'].rolling(window=20).mean()
            data['Upper_Band'] = data['Middle_Band'] + 2 * data['Close'].rolling(window=20).std()
            data['Lower_Band'] = data['Middle_Band'] - 2 * data['Close'].rolling(window=20).std()

            data_dict[ticker] = data
        except Exception as e:
            print(f"Failed to load data from CSV for {ticker}: {e}")
    return data_dict

def predict_price_from_csv(ticker):
    data = get_technical_indicators_from_csv([ticker])[ticker]

    # Feature Engineering
    data['Next_Close'] = data['Close'].shift(-1)  # Shift the Close price to the next day
    data.dropna(inplace=True)  # Drop NaN values

    X = data[['SMA', 'Upper_Band', 'Lower_Band']]  # Features: Simple Moving Average, Upper Bollinger Band, Lower Bollinger Band
    y = data['Next_Close']  # Target: Next day's Close price

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Model Training
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Model Evaluation
    y_pred_train = model.predict(X_train)
    y_pred_test = model.predict(X_test)

    train_rmse = np.sqrt(mean_squared_error(y_train, y_pred_train))
    test_rmse = np.sqrt(mean_squared_error(y_test, y_pred_test))

    # print(f"Train RMSE: {train_rmse}")
    # print(f"Test RMSE: {test_rmse}")

    # Predict next day's Close price
    last_sma = data['SMA'].iloc[-1]
    last_upper_band = data['Upper_Band'].iloc[-1]
    last_lower_band = data['Lower_Band'].iloc[-1]
    next_close_pred = model.predict([[last_sma, last_upper_band, last_lower_band]])
    # print(next_close_pred[0])
    return(next_close_pred[0])

