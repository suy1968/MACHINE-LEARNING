import pandas as pd
data = pd.read_csv('https://tinyurl.com/titanic-csv')
print(data.loc[:4,'Name':'Survived'])
