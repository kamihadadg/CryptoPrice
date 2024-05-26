from KYfinance import get_technical_indicators as yf
from algo1 import predict_price_from_csv as PrP
from algo2 import predict_price_from_csv as pbol
from algo3 import trainticker as pboltr




import warnings
warnings.filterwarnings("ignore", category=UserWarning)

tickers = ['BTC-USD', 'ETH-USD', 'ADA-USD','ICP-USD','GC=F','CL=F']
# Call the function to retrieve data and calculate indicators
ticker_data = yf(tickers, '1y')

# # Print information for each ticker
# for ticker, data in ticker_data.items():
#     print(f"Technical Indicators for {ticker}:")
#     print(data)

# Predict price for each ticker
for ticker in tickers:
    PrP(ticker)
    pbol(ticker)
    pboltr(ticker)
