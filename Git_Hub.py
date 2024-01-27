import yfinance as yf
symbol = 'aapl'
stock_data = yf.download(symbol,start = '2022-01-01', end = '2022-12-31')
print(stock_data.head())