import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

s = pd.Series([1,3,5,np.nan,6,8])
print(s)

dates = pd.date_range('20130101', periods=6)
print(dates)

df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
print(df)

#print(pd.read_csv('daily.csv'))
#print(pd.read_csv('companies.csv'))

daily_df=pd.read_csv('daily.csv')
print(daily_df)

companies_df = pd.read_csv('companies.csv')
print(companies_df)

mergedData = pd.merge(daily_df, companies_df)

print(mergedData.sort_values(by='date'))

mergedData['date'] = pd.to_datetime(mergedData.date)
print(mergedData.sort_values(by='date'))

idx = pd.date_range('01-01-2017', '01-10-2017')
mergedData.index = pd.DatetimeIndex(mergedData.index)
mergedData = mergedData.reindex(idx, fill_value='NaT')

print(mergedData)
