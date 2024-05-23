import yfinance as yf
import pandas_ta as ta

# دریافت داده‌های بیت‌کوین از Yahoo Finance
ticker = 'BTC-USD'
data = yf.download(ticker, period='1mo', interval='1d')

# محاسبه اندیکاتورهای تکنیکال
data['SMA'] = ta.sma(data['Close'], length=14)  # میانگین متحرک ساده
data['RSI'] = ta.rsi(data['Close'], length=14)  # شاخص قدرت نسبی

print(data)
