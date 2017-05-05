import pandas as pd
import numpy as np
import matplotlib.pyplot as plt        

file1 = 'daily.csv'
file2 = 'companies.csv'
finalfile = 'merged.csv'
start_date = '1/4/17'
end_date = '1/8/17'

daily_df = pd.read_csv(file1)
print(daily_df)

companies_df = pd.read_csv(file2)
print(companies_df)

mergedData = pd.merge(daily_df, companies_df)

print(mergedData.sort_values(by='date'))

mergedData['date'] = pd.to_datetime(mergedData.date)
print(mergedData.sort_values(by='date'))

mergedData['difference'] = mergedData['value'] - mergedData['value'].shift(1)
print(mergedData.sort_values(['date', 'id'], ascending=[True,True]))

mergedData.to_csv(finalfile, sep=',', mode='w')


