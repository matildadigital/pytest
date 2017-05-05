import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#print(pd.read_csv('daily.csv'))
#print(pd.read_csv('companies.csv'))

file = 'daily.csv'

#daily_df = pd.read_csv(file, sep=',', parse_dates=[1], index_col='date', dayfirst = False)

daily_df = pd.read_csv(file)
print(daily_df)
daily_df['date'] = pd.to_datetime(daily_df['date'])
daily_df = daily_df.sort_values(by=['date'], ascending=[True])
daily_df.set_index('date', inplace=True)
print(daily_df)

daily_df = daily_df.resample('D', on='date').bfill()
print(daily_df)

'''idx = pd.date_range('01-01-2017', '01-10-2017')
daily_df.index = pd.DatetimeIndex(daily_df.index)
daily_df = daily_df.reindex(idx, fill_value = 'NaN')
print(daily_df)'''

companies_df = pd.read_csv('companies.csv')
print(companies_df)

'''mergedData = pd.merge(daily_df, companies_df)

print(mergedData.sort_values(by='date'))

mergedData['date'] = pd.to_datetime(mergedData.date)
print(mergedData.sort_values(by='date'))


mergedData.index = pd.DatetimeIndex(mergedData.index)
mergedData = mergedData.reindex(idx, fill_value='NaT')

print(mergedData)'''
