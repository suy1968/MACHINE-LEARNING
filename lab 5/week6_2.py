import pandas as pd
data = pd.read_csv('https://tinyurl.com/titanic-csv')
print(data.iloc[:7])
print(data.loc[1:7,'PClass':'Survived'])
