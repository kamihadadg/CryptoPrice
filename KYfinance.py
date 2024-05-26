import yfinance as yf
import pandas_ta as ta

def get_technical_indicators(tickers,aperiod):
    # یک دیکشنری برای ذخیره داده‌های هر تیکر
    data_dict = {}

    # حلقه برای دریافت داده‌ها و محاسبه اندیکاتورها برای هر تیکر
    for ticker in tickers:
        try:
            # دریافت داده‌ها از Yahoo Finance
            data = yf.download(ticker, period=aperiod, interval='1d')

            data.to_csv('data\\'+ticker+'.csv')
            # پر کردن مقادیر گم شده
            data.ffill(inplace=True)  # Fill missing values with previous value

            # محاسبه اندیکاتورهای تکنیکال
            data['SMA'] = ta.sma(data['Close'], length=14)  # Simple Moving Average
            data['RSI'] = ta.rsi(data['Close'], length=14)  # Relative Strength Index

            # MACD (Moving Average Convergence Divergence)
            # macd = ta.macd(data['Close'], fast=12, slow=26, signal=9)
            # data['MACD'] = macd['MACD_12_26_9']
            # data['MACD_Signal'] = macd['MACDs_12_26_9']
            # data['MACD_Hist'] = macd['MACDh_12_26_9']

            # Bollinger Bands (BBands)
            bbands = ta.bbands(data['Close'], length=20, std=2)
            data['BB_Upper'] = bbands['BBU_20_2.0']
            data['BB_Middle'] = bbands['BBM_20_2.0']
            data['BB_Lower'] = bbands['BBL_20_2.0']

            # Average True Range (ATR)
            data['ATR'] = ta.atr(data['High'], data['Low'], data['Close'], length=14)

            # Ichimoku Cloud (optional)
            # ichimoku = ta.ichimoku(data['High'], data['Low'], data['Close'])
            # data['Ichimoku_Conversion'] = ichimoku['ISA_9']
            # data['Ichimoku_Base'] = ichimoku['ISB_26']
            # data['Ichimoku_SpanA'] = ichimoku['ITS_9']
            # data['Ichimoku_SpanB'] = ichimoku['IKS_26']
            # data['Ichimoku_Lagging'] = ichimoku['ICS_26']

            # ذخیره داده‌های تیکر در دیکشنری
            data_dict[ticker] = data

        except Exception as e:
            print(f"Failed to download data for {ticker}: {e}")

    return data_dict


# 