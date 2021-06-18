import pandas as pd
data = pd.read_csv('https://tinyurl.com/titanic-csv')
print(data['PClass'].unique)
print(data['Age'].value_counts())
print(data['PClass'].value_counts())
