import pandas as pd
import numpy as np
import matplotlib.pyplot as plt        

file1 = 'daily.csv'
file2 = 'companies.csv'
finalfile = 'merged.csv'
start_date = '1/3/17'
end_date = '1/8/17'

start_date = pd.to_datetime(start_date)
end_date = pd.to_datetime(end_date)

daily_df = pd.read_csv(file1)
print(daily_df)

companies_df = pd.read_csv(file2)
print(companies_df)

mergedData = pd.merge(daily_df, companies_df)
print(mergedData.sort_values(by='date'))

mergedData['date'] = pd.to_datetime(mergedData.date)
mergedData = mergedData[(mergedData['date'] >= start_date) & (mergedData['date'] <= end_date)]
print(mergedData.sort_values(by='date'))

mergedData['difference'] = mergedData['value'] - mergedData['value'].shift(1)
mergedData = mergedData.sort_values(['date', 'id'], ascending=[True,True])
print(mergedData)

mergedData.to_csv(finalfile, sep=',', mode='w')


