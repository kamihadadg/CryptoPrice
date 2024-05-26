from KYfinance import get_technical_indicators as yf
from algo1 import predict_price_from_csv as PrP
from algo2 import predict_price_from_csv as pbol
from algo3 import trainticker as pboltr
from bs4 import BeautifulSoup

import warnings
warnings.filterwarnings("ignore", category=UserWarning)

tickers = ['BTC-USD', 'ETH-USD', 'ADA-USD','ICP-USD','GC=F','CL=F']
ticker_data = yf(tickers, '1y')
output_html = 'output.html'

# Create an HTML document
html_content = """
<html>
<head>
    <title>Stock Predictions</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            padding: 20px;
            background-color: #f7f7f7;
        }
        table {
            border-collapse: collapse;
            width: 100%;
            border: 2px solid #ddd;
            border-radius: 8px;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 12px;
            text-align: left;
        }
        th {
            background-color: #f2f2f2;
            font-weight: bold;
        }
        .prediction {
            font-weight: bold;
            color: #008000; /* Green color for predicted prices */
        }
        .na {
            color: #888;
        }
        tr:nth-child(even) {
            background-color: #f9f9f9; /* Alternate row background color */
        }
        tr:hover {
            background-color: #f2f2f2; /* Hover effect */
        }
    </style>
</head>
<body>
<table>
    <tr>
        <th>Ticker</th>
        <th>Predicted Price 1</th>
        <th>Predicted Price 2</th>
        <th>Predicted Price 3</th>
    </tr>
"""

# Predict price for each ticker and append to HTML table
for ticker in tickers:
    predicted_price1 = PrP(ticker)
    predicted_price2 = pbol(ticker)
    predicted_price3 = pboltr(ticker)
    html_content += f"<tr>"
    html_content += f"<td>{ticker}</td>"
    html_content += f"<td class=\"{'prediction' if predicted_price1 is not None else 'na'}\">{'' if predicted_price1 is None else format(predicted_price1, ',.4f')}</td>"
    html_content += f"<td class=\"{'prediction' if predicted_price2 is not None else 'na'}\">{'' if predicted_price2 is None else format(predicted_price2, ',.4f')}</td>"
    html_content += f"<td class=\"{'prediction' if predicted_price3 is not None else 'na'}\">{'' if predicted_price3 is None else format(predicted_price3, ',.4f')}</td>"
    html_content += f"</tr>"

# Close HTML table and document
html_content += """
</table>
</body>
</html>
"""

# Write HTML content to a file
with open(output_html, 'w') as file:
    file.write(html_content)

# Open HTML file in default web browser
# import webbrowser
# webbrowser.open('file://' + output_html)

# Predict price for each ticker
for ticker in tickers:
    PrP(ticker)
    pbol(ticker)
    pboltr(ticker)
