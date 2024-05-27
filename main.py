from flask import Flask, jsonify, render_template
from KYfinance import get_technical_indicators as yf
from algo1 import predict_price_from_csv as PrP
from algo2 import predict_price_from_csv as pbol
from algo3 import trainticker as pboltr
import warnings

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
    


if __name__ == '__main__':
    app.run(debug=True)
