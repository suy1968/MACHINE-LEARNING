import pandas as pd
data = pd.read_csv('https://tinyurl.com/titanic-csv')
d1 = data.rename(columns = {'Sex':'Gender'})
print(d1.head())
data.rename(columns = {'Sex':'Gender'},inplace = True)
print(data.head())
