from flask import Flask, jsonify, render_template
from KYfinance import get_technical_indicators as yf
from algo1 import predict_price_from_csv as PrP
from algo2 import predict_price_from_csv as pbol
from algo3 import trainticker as pboltr
import warnings
import requests

warnings.filterwarnings("ignore", category=UserWarning)

app = Flask(__name__)

tickers = ['BTC-USD', 'ETH-USD', 'ADA-USD', 'ICP-USD', 'GC=F', 'CL=F']

@app.route('/fetchdb', methods=['GET'])
def getdb():
    yf(tickers, '1y')
    return jsonify('Ok')

@app.route('/predictions', methods=['GET'])
def get_predictions():
    predictions = {}
    for ticker in tickers:
        predicted_price1 = PrP(ticker)
        predicted_price2 = pbol(ticker)
        predicted_price3 = pboltr(ticker)
        predictions[ticker] = {
            'Predicted Price 1': None if predicted_price1 is None else format(predicted_price1, ',.4f'),
            'Predicted Price 2': None if predicted_price2 is None else format(predicted_price2, ',.4f'),
            'Predicted Price 3': None if predicted_price3 is None else format(predicted_price3, ',.4f')
        }
    return jsonify(predictions)

@app.route('/', methods=['GET'])
def get_predictions_html():
    predictions = {}
    for ticker in tickers:
        predicted_price1 = PrP(ticker)
        predicted_price2 = pbol(ticker)
        predicted_price3 = pboltr(ticker)
        predictions[ticker] = {
            'Predicted Price 1': None if predicted_price1 is None else format(predicted_price1, ',.4f'),
            'Predicted Price 2': None if predicted_price2 is None else format(predicted_price2, ',.4f'),
            'Predicted Price 3': None if predicted_price3 is None else format(predicted_price3, ',.4f')
        }
    
    return render_template('predictions.html', predictions=predictions)
    
@app.route('/exchange_rates', methods=['GET'])
def get_exchange_rates():

    
    # url = "https://openexchangerates.org/api/latest.json?app_id=a999320ecbe146e596a42c569297004e"

    # headers = {"accept": "application/json"}

    # response = requests.get(url, headers=headers)

    # print(response.text)
    
    
    endpoint = f"https://open.er-api.com/v6/latest"
    response = requests.get(endpoint)
    if response.status_code == 200:
        data = response.json()
        return jsonify(data)
    else:
        return jsonify({'error': 'Failed to fetch exchange rates'})
    
@app.route('/crypto_price', methods=['GET'])
def get_cryptoprice():

   # Fetch exchange rates from CoinGecko API
    endpoint = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        'ids': 'bitcoin,ethereum,cardano,internet-computer',
        'vs_currencies': 'usd'
    }
    response = requests.get(endpoint, params=params)
    if response.status_code == 200:
        data = response.json()
        return jsonify(data)
    else:
        return jsonify({'error': 'Failed to fetch exchange rates'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

