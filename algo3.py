import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def prepare_data(ticker, window_size=20):
    # Download data
    data = pd.read_csv('data\\'+ticker + '.csv', index_col=0)  # Load data from CSV
    data.ffill(inplace=True)
    # Feature scaling
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(data['Close'].values.reshape(-1,1))

    # Create input and target sequences
    X, y = [], []
    for i in range(len(scaled_data) - window_size):
        X.append(scaled_data[i:i+window_size, 0])
        y.append(scaled_data[i+window_size, 0])

    X, y = np.array(X), np.array(y)

    return X, y, scaler

def train_model(X_train, y_train):
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model

def predict_price(model, X_test, scaler, window_size=20):
    last_window = X_test[-window_size:]
    predicted_price = model.predict(last_window.reshape(1, -1))
    predicted_price = scaler.inverse_transform(predicted_price.reshape(-1, 1))
    return predicted_price


# Example usage:
def trainticker(ticker):

    window_size = 20
    X, y, scaler = prepare_data(ticker, window_size=window_size)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = train_model(X_train, y_train)

    predicted_price = predict_price(model, X_test[-1], scaler)
    # print(predicted_price[0][0])
    return(predicted_price[0][0])
