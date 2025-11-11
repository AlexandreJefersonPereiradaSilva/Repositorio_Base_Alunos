import pandas as pd
import datetime
ds = pd.read_csv('btcusd_1-min_data.csv')

print(ds.head())

print(ds.tail())
'''
x = ds['Timesstamp'].apply(lambda h)
y = ds['High'] > 5.0
print(y)
'''


