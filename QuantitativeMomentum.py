'''A quantitative momentum investing strategy.  Selects the 50 stocks with the highest price momentum.  
   Calculates recommended trades for equal weighted portfolio of the stocks.'''

import numpy as np 
import pandas as pd 
import requests 
import xlsxwriter 
import math 
from secrets import IEX_CLOUD_API_TOKEN
from scipy import stats 
from utilities import chunks

# Import list of stocks into pandas series 
stocks = pd.read_csv('sp_500_stocks.csv')

symbol_string = 'AAPL'
api_url = f'https://sandbox.iexapis.com/stable/stock/{symbol_string}/stats?token={IEX_CLOUD_API_TOKEN}'
data = requests.get(api_url).json()
print(data['year1ChangePercent'])

symbol_groups = list(chunks(stocks['Ticker'], 100))
symbol_strings = []
for i in range(0, len(symbol_groups)):
    symbol_strings.append(','.join(symbol_groups[i]))


my_columns = ['Ticker', 'Price,', 'One-Year Price Return', 'Number of Shares to Buy']